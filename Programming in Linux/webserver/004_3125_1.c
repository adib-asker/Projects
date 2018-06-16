#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/select.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/uio.h>
#include <sys/wait.h>
#include <sys/sendfile.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>
#include <fnmatch.h>
#include <limits.h>
#include <errno.h>

static int num_forks = 0;
static int serve_flag = 1;  //flag for main server loop
static int server_sock = 0;	// main server socket, used to accept client HTTP requsts
static pid_t srv_pid = 0;	  //

#define BACKLOG 10

//2Kb buffer size for request
#define REQUEST_MAX_SIZE 2048

int make_server_skt(const unsigned short port){
  struct sockaddr_in addr;
  int server_sock;

  server_sock = socket(AF_INET, SOCK_STREAM, 0);
  if(server_sock < 0) {
      perror("socket");
      return -1;
  }

  /* This fails 'Test 2' ?
  int reuse_true = 1;
  if (setsockopt(server_sock, SOL_SOCKET, SO_REUSEADDR, &reuse_true, sizeof(int)) < 0) {
      perror("setsockopt");
      return -1;
  }*/

  addr.sin_family = AF_INET;
  addr.sin_port = htons(port); // byte order is significant
  addr.sin_addr.s_addr = INADDR_ANY; // listen to all interfaces

  if(bind(server_sock, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
      perror("bind");
      return -1;
  }

  if(listen(server_sock, BACKLOG) < 0) {
      perror("listen");
      return -1;
  }

  return server_sock;
};

ssize_t read_headers(int fd, void *vptr, size_t n){
	char *ptr = vptr;

	size_t nleft = n;
	while (nleft > 0) {
		ssize_t nread;
		if ((nread = read(fd, ptr, 1)) < 0) {
			if (errno == EINTR) // if get interrupted by a signal
				nread = 0; // just call read again
			else
				return -1;
		}else if (nread == 0)	// read returned EOF
			break;

		nleft -= nread;

		if(strstr(vptr, "\r\n\r\n") != NULL){
			return n - nleft;
		}
		ptr += nread;
	}
	return n - nleft;
}

ssize_t writen(int fd, void *vptr, size_t n){

	const char *ptr = vptr;
	size_t nleft = n;

	while (nleft > 0) {
		ssize_t nwritten;
		if ((nwritten = write(fd, ptr, nleft)) <= 0) {
			if (errno == EINTR) // if get interrupted by a signal
				nwritten = 0;
			else
				return -1;
		}
		nleft -= nwritten;
		ptr += nwritten;
	}
	return n;
}

static const char * find_content_type(const char * filename){
  //last entry is used as default
  static const char * extension_content_types[7*2] =
  {
  	"htm",  "text/html",
  	"html",  "text/html", /* html or htm extension*/
    "css",   "text/css",  /* css extension */
    "jpeg",  "image/jpeg",/* jpg extension */
    "png",  "image/png",  /* png extension */
    "gif",  "image/gif",  /* gif extension */
    "txt",  "text/plain", /* Any other extensions */
  };

  //iterate to file extension (.txt)
  int i, ext_start;
	ext_start = strlen(filename);
	while((--ext_start > 0) && (filename[ext_start] != '.'));
	ext_start++;

  //compare it to our array of extension
	for(i=0; i < 7*2; i+=2){
		if(strcmp(&filename[ext_start], extension_content_types[i]) == 0){
			return extension_content_types[i+1];
		}
	}

	return extension_content_types[(7*2) - 1];
}

static int parse_headers(int sfd, char* buf, const int buf_size){
	int total = 0;
  int bytes = read_headers(sfd, buf, buf_size);
  switch(bytes){
  	case -1:
  		perror("recv");
  		close(sfd);
  		break;
  	case  0:
  		fprintf(stderr, "Socket was closed from remote side\n");
  		close(sfd);
    	break;
  	default:
  		total += bytes;
  		break;
	}


	buf[total] = '\0';
	return total;
};

static int handle_file_request(int sfd, char * filename, char * buf, const int alive, int code){

	int fd = open(filename, O_RDONLY);
	if(fd == -1){
		perror("open");

    code = 404;
    strncpy(filename, "e404.html", PATH_MAX);

    fd = open(filename, O_RDONLY);
    if(fd == -1){
  		perror("open2");
      return 0;
    }
	}

  struct stat st;
  stat(filename, &st);
  off_t file_size = st.st_size;

  //send resonse header
  int len;
  switch(code){
      case 404:
        len = snprintf(buf, REQUEST_MAX_SIZE, "HTTP/1.1 404 Not Found\r\n");
        //if(alive) file_size = 0;
        break;
      case 501:
        len = snprintf(buf, REQUEST_MAX_SIZE, "HTTP/1.1 501 Not Implemented\r\n");
        //if(alive) file_size = 0;
        break;
      case 200:
      default:
        len = snprintf(buf, REQUEST_MAX_SIZE, "HTTP/1.1 200 OK\r\n");
        break;
  }

  len += snprintf(&buf[len], REQUEST_MAX_SIZE-len, "Connection: %s\r\n", (alive) ? "keep-alive" : "close");

  const char * type = find_content_type(filename);
  len += snprintf(&buf[len], REQUEST_MAX_SIZE-len, "Content-Type: %s\r\nContent-Length: %lu\r\n\r\n", type, file_size);

  writen(sfd, buf, len);  //send headers to client

	off_t offset = 0;
	while(offset < file_size){
    ssize_t bytes = sendfile(sfd, fd, &offset, file_size - offset);
    //fprintf(stderr, "Sent %lu bytes from %s\n", file_size, filename);
		if(bytes == -1){
			perror("sendfile");
			break;
		}
	}
  //printf("Done\n");
	close(fd);  //close file

	return 0;
};

static void fix_filename(char * filename){

  int i=0;
	while((filename[i] == '/')  || (filename[i] == '.')) i++;

  int j;
	for(j=0; filename[j] != '\0'; j++, i++){
		filename[j] = filename[i];
	}

	if(filename[0] == '\0'){
		filename[0] = '.';
		filename[1] = '\0';
	}
}

//Function for handlina a client connection
void handle_session(int sfd){	//sess is the connection socket identifier

	char buf[REQUEST_MAX_SIZE];
	char filename[PATH_MAX];

  while(1){ //while connection is open

    bzero(buf, REQUEST_MAX_SIZE);
    bzero(filename, PATH_MAX);

  	if(parse_headers(sfd, buf, REQUEST_MAX_SIZE) <= 0)
      break;  //if we failed to parse or socket was closed

    printf("%s\n", buf);

    int code = 200, keep_alive = 0;
  	if(fnmatch("GET * HTTP/1.*", buf, 0) != 0){
      code = 501;
      strncpy(filename, "e501.html", PATH_MAX); //redirect to error file
    }else{  //its a GET request
      if( strstr(buf, "Connection: Keep-Alive") ||
          strstr(buf, "Connection: keep-alive")){
        keep_alive = 1;
      }
      //extract filename
      sscanf(buf, "GET %s HTTP/1.", filename);
    	fix_filename(filename);	//remove leading /.
    }

  	//fprintf(stderr, "Request for file '%s'\n", filename);

    struct stat fst;
  	stat(filename, &fst);

  	if(S_ISDIR(fst.st_mode)){	//if its a directory
      //redirect to error file
  		snprintf(buf, sizeof(buf), "%s/index.html", filename);
      strncpy(filename, buf, PATH_MAX);

  		//check for index.html
  		if(access(filename, R_OK) != 0){	//we have index file
        code = 404;
        strncpy(filename, "e404.html", PATH_MAX); //redirect to error file
  		}
      stat(filename, &fst);
  	}

    //send requested file to client
    handle_file_request(sfd, filename, buf, keep_alive, code);
  }

  //close the socket gracefully
  shutdown(sfd, SHUT_RDWR);
	close(sfd);
}

//Function for handling signals the process receives
//signo is the signal number
static void sig_handler(int signo){
	switch(signo){
		case SIGINT:	//interrupt signal
		case SIGHUP:
		  //break;
		case SIGQUIT:
		case SIGTERM:	//terminate signal
      serve_flag = 0; //stop main loop
			printf("Interrupt received ...\n");
			break;
		case SIGCHLD:	//child stopped or terminated
			while(waitpid(-1, NULL, WNOHANG) < 0); //call wait to clear its resources
			num_forks--;
			break;
	}
};

int main(const int argc, const char* argv[]) {

	if(argc != 2){
		fprintf(stderr, "Usage: %s <port_number>\n", argv[0]);
		return EXIT_FAILURE;
	}

  //get first argument
  int port = atoi(argv[1]);

	srv_pid = getpid(); //save server pid

  //catch interrupts from user
	struct sigaction act, act_old;	//structures for holding sigaction parameters
		act.sa_handler = sig_handler;	//function to be called when a signal is received
		act.sa_flags = SA_NOCLDSTOP;
		sigemptyset(&act.sa_mask);
		if(	(sigaction(SIGINT,  &act, &act_old) == -1)	||		//del | Ctrl-c
				(sigaction(SIGTERM, &act, &act_old) == -1)  ||
				(sigaction(SIGCHLD, &act, &act_old) == -1)	){	// zombie destroying
			perror("signal");
			exit(EXIT_FAILURE);
		}

  //run server in our web content directory
	if(chdir("web") < 0){
		perror("chdir");
		return 1;
	}

  server_sock = make_server_skt(port);
  if(server_sock < 0){
    return EXIT_FAILURE;
  }

  while(serve_flag) {
    struct sockaddr_in remote_addr;
    unsigned int socklen = sizeof(remote_addr);

    int sock = accept(server_sock, (struct sockaddr*) &remote_addr, &socklen);
    if(sock < 0) {
      perror("accept");
      break;
    }

    pid_t pid = fork();
    if(pid == 0){ //child
      handle_session(sock); //process client HTTP request
      exit(EXIT_SUCCESS);   //child is done
    }else if(pid > 0){  //parent
      num_forks++;
    }else{
      perror("fork");
      break;
    }
  }

	close(server_sock);

  //clear zombies
  while(num_forks > 0){
    waitpid(-1, NULL, WNOHANG);
		num_forks--;
	}

	return 0;
}
