#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piyobjnfsstaasSS
import piyobjsshfsstaasSS
import piyobjgfsstaasSS

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19931))

def objstaasSS(c,addr,cusname):
	while True:
		c.sendall(""" \n\t\t We provide Following Method of Object STAAS :
		\t\t 1. Network File System
		\t\t 2. SSH File System
		\t\t 3. Gluster File System
		\t\t 4. Exit
		\nWhich Method you want Enter the choice {1,2,3,4} : """)
		obtype=c.recv(20).strip()  

	        if  int(obtype) == 1:
			piyobjnfsstaasSS.objnfsstaasSS(c,addr,cusname)
		elif  int(obtype) == 2:
		        piyobjsshfsstaasSS.objsshfsstaasSS(c,addr,cusname)
                elif  int(obtype) == 3:
		        piyobjgfsstaasSS.objgfsstaasSS(c,addr,cusname)
 		elif int(obtype) == 4:
                        break
 		else:
 		     c.send( """ You have selected Wrong Choice 
		       Please Select Correct Choice """ )
                     continue
                c.close()

