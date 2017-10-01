#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piyRHServicesCS

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 30001))

def tyosREDHATCS(s1,unamm):
	while True:
                dt30=s1.recv(2000)
                sys.stdout.write(dt30)
		costyp=raw_input()
                s1.sendall(costyp)
	        if  int(costyp) == 1:
			piyRHServicesCS.RHServicesCS(s1,unamm)
 		elif int(opt)==2:
			pass           #to go back
		elif int(opt)==3:
			print"\n Thanku Very Much For using Our Services \n"
			c.close()
			sys.exit()
 		else:
 		     print ( """ You have selected Wrong Choice 
		       Please Select Correct Choice """ )
                     continue
                s1.close()

