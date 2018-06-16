#Name: Sk Adib Asker

#Class Section: 006

#!/usr/bin/python

import sys
import socket
import signal
import time
import re
import os.path

def start_server(host, port, www_dir):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
    except Exception as e:
        sys.stderr.write("Error: Failed to start server\n")
        s.shutdown(socket.SHUT_RDWR)
        sys.exit(1)
    return s

def listen_for_request(s, www_dir):

    while True:

        s.listen(1) # maximum number of queued connections

        conn, addr = s.accept()

        (peer_host, peer_port) = conn.getpeername()
        print peer_host + " connected"

        req = conn.recv(1024) #receive data from client
        #string = bytes.decode(data) #decode it to string


        #GET /filename.html HTTP/1.1\r\n
        meth,path,ver = req.split(' ', 2)
        if meth != 'GET':
            sys.stderr.write('Unknown request method ' + meth + '\n')
            conn.shutdown()
            continue

        file_path = www_dir + path

        #if path is not a file, return 404
        if not os.path.isfile(file_path):
            sys.stderr.write('[404]: ' + file_path + '\n')

            hdr = 'HTTP/1.1 404 Not Found\r\n'
            hdr+= 'Date: ' + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()) +'\r\n'
            hdr+= '\r\n'
            conn.send(hdr)
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            continue

        f_mtime = os.path.getmtime(file_path)

        #If-Modified-Since: Fri, 02 Mar 2018 21:06:02 GMT\r\n
        result = re.search('If-Modified-Since: (.*)\r\n', req)
        if result:
            last_mod_time = result.group(1)

            ftm = time.strptime(last_mod_time, "%a, %d %b %Y %H:%M:%S %Z")
            req_mtime = time.mktime(ftm)

            #print("R=%d, F=%d\n" % (req_mtime, f_mtime))

            if req_mtime == f_mtime:
                sys.stdout.write('[304]: ' + file_path + '\n')

                hdr = 'HTTP/1.1 304 Not Modified\r\n'
                hdr+= 'Date: ' + time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", time.gmtime())
                hdr+= '\r\n'
                conn.send(hdr)
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                continue

        ## Load file content
        f = open(file_path, 'rb')
        fdata = f.read() # read file content
        f.close()

        sys.stdout.write('[200]: ' + file_path + '\n')
        hdr = 'HTTP/1.1 200 OK\r\n'
        hdr+= 'Date: ' + time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", time.gmtime())

        ftm = time.gmtime(f_mtime)
        hdr+= 'Last-Modified: ' + time.strftime("%a, %d %b %Y %H:%M:%S %Z\r\n", ftm)

        hdr+= '\r\n'
        hdr+= fdata

        conn.send(hdr)
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

def graceful_shutdown(sig, dummy):
    s.shutdown(socket.SHUT_RDWR)
    sys.exit(1)

#-------------------------------------------------#

#If you server doesn't have GMT, we need to set it to GMT timezone, just for script
os.environ['TZ'] = 'Europe/London'
time.tzset()

if len(sys.argv) != 3:
    sys.stderr.write('Usage: server.py <port> <www_dir>\n')
    sys.exit(1)

host = ''
port = int(sys.argv[1])
www_dir = sys.argv[2]

# shut down on ctrl+c
signal.signal(signal.SIGINT, graceful_shutdown)

s = start_server(host, port, www_dir) # aquire the socket
listen_for_request(s, www_dir)

s.shutdown(socket.SHUT_RDWR)
sys.exit(0)
