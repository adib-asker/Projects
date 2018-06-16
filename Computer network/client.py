#Name: Sk Adib Asker

#Class Section: 006

#!/usr/bin/python

import socket
import sys
import datetime, time
import re

def get_file(host, port, path, last_mod):
    #print 'Connecting to '+ host + ':' + port

    # Set up a TCP/IP socket and connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,int(port)))

    # Protocol exchange - sends and receives
    req_msg = "GET /" + path +" HTTP/1.0\r\n"
    req_msg+= 'Host: ' + host + ':' + port + '\r\n'

    if last_mod:
        req_msg += 'If-Modified-Since: ' + last_mod + '\r\n'

    req_msg+= '\r\n'

    print req_msg

    s.sendall(req_msg)

    last_mod = ''
    while True:
        resp = s.recv(1024)

        #save last modified header
        result = re.search('Last-Modified: (.*)\r\n', resp)
        if result:
            last_mod = result.group(1)

        if resp == "":
            break
        print resp

    s.close()   # Close the connection when completed

    return last_mod

#-------------------------------------------------#

if len(sys.argv) != 2:
    sys.stderr.write('Usage: client.py <localhost:12000/filename.html>\n')
    sys.exit(1)

#https://docs.python.org/2/library/re.html
host,port, path = re.split("[:/]", sys.argv[1], 2)

#print 'Requesting /' + path

last_mod = get_file(host, port, path, '')
get_file(host, port, path, last_mod)
