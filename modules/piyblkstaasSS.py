#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piyblkiscsistaasSS

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19935))

def blkstaasSS(c,addr,cusname):
	while True:
		c.sendall(""" \n\t\t We provide Following Method of Block STAAS :
		\t\t 1. Internet Small Computer System Interface
		\t\t 2. Exit
		\nWhich Method you want Enter the choice {1,2} : """)
		bktype=c.recv(20).strip()  

	        if  int(bktype) == 1:
			piyblkiscsistaasSS.blkiscsistaasSS(c,addr,cusname)
 		elif int(bktype) == 2:
                      break
 		else:
 		     c.send( """ You have selected Wrong Choice 
		       Please Select Correct Choice """ )
                     continue
                c.close()

