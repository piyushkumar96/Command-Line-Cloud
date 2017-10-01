#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piystaasCS
import piysaassshCS   # SAAS
import os

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 40001))

def RHServicesCS(s1,unamm):
	while True:
		os.system("clear")
		data31=s1.recv(3000)
		sys.stdout.write(data31)

                choice=raw_input()
		s1.send(""+choice)

		data1=s1.recv(100)
		sys.stdout.write(data1)

		if   int(choice)==1:
			piysaassshCS.saassshCS(s1,unamm)
		elif int(choice)==2:
			s1.send( " You have selected INFRASTRUCURE AS A SERVICE " )
		elif int(choice)==3:
			piystaasCS.staasCS(s1,unamm)	       
		elif int(choice)==4:
			s1.send( " You have selected DATABASE AS A SERVICE ")
		elif int(choice)==5:
			s1.send( " You have selected PLATFORM AS A SERVICE ")
		elif int(choice)==6:
			print ( """ Thanku Very Much For Using Our Services  
				  See You Soon                   """ )
		else:
			s1.send( """ You have selected Wrong Choice 
			       Please Select Correct Choice """ )
                s1.close()

