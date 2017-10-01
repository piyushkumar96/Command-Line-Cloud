#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piyblkstaasSS
import piyobjstaasSS
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19930))

def staasSS(c,addr,cusname):
		c.sendall(""" \n\t\t We provide Following Types of Staas Services :
		\t\t 1. Object As STAAS
		\t\t 2. Block As STAAS
		\t\t 3. Exit
		\nWhich Types of Staas Services you want Enter the choice {1,2,3} : """)
		tyst=c.recv(20).strip() 
	        if  int(tyst) == 1:
			piyobjstaasSS.objstaasSS(c,addr,cusname)
		elif  int(tyst) == 2:
		    	piyblkstaasSS.blkstaasSS(c,addr,cusname)
			pass
 		elif int(tyst) == 3:
                        pass
 		else:
 		        print ( """ You have selected Wrong Choice 
		                       Please Select Correct Choice """ )    
                c.close()

