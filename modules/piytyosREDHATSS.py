#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piyRHServicesSS

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("",30000 ))

def tyosREDHATSS(c,addr,cusname):
	while True:
		c.sendall(""" \n\t\t\t\t  MENU  :
		\t\t 1. To See Service Provided By Us For Redhat
		\t\t 2. To go Back Type back 
		\t\t 3. To Exit Type exit
	      \t\t Enter the Choice  : """)
		opt=string.lower(c.recv(20).strip())  
		if int(opt)==1:
			piyRHServicesSS.RHServicesSS(c,addr,cusname)
		elif int(opt)==2:
			pass
		elif int(opt)==3:
			print"\n Thanku Very Much For using Our Services \n"
			c.close()
			sys.exit()
		else:
			c.sendall( """ You have selected Wrong Choice 
					       Please Select Correct Choice """ )
				     
                c.close()

#thread.start_new_thread(saassshSS ,(c,addr))


	

