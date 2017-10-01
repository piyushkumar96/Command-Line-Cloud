#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piyblkiscsistaasCS

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19925))

def blkstaasCS(s1):
	while True:
                data6=s1.recv(3000)
                sys.stdout.write(data6)
		cbktype1=raw_input()
                s1.sendall(cbktype1)
	        if  int(cbktype1) == 1:
			piyblkiscsistaasCS.blkiscsistaasCS(s1)
 		elif int(cbktype1) == 2:
                      break
 		else:
 		     print ( """ You have selected Wrong Choice 
		       Please Select Correct Choice """ )
                     continue
                s1.close()

