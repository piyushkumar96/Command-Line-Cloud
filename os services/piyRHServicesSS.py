#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import time
import piysaassshSS
import piystaasSS

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("",40000 ))

def RHServicesSS(c,addr,cusname):
	while True:
		c.sendall(
		"""\n\t\t\t\t  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		\t\t  @@@        Piyush---Cloud        @@@
		\t\t  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n
		\t\t######    Services Provided         ######\n
		\t\t####  1. SOFTWARE AS A SERVICE        ####
		\t\t####  2. INFRASTRUCURE  AS A SERVICE  ####
		\t\t####  3. STORAGE AS A SERVICE         ####
		\t\t####  4. DATABASE AS A SERVICE        ####
		\t\t####  5. PLATFORM AS A SERVICE        ####
		\t\t####  6. EXIT                         ####
		\t\t######   ENTER THE CHOICE :-       ####### """)  
		#execfile("/root/Desktop/project/cloud/USER_MANUAL.py")
		ch=c.recv(20).strip()

		if   int(ch)==1:
			c.sendall( "\n You have selected SOFTWARE AS A SERVICE \n ")
			piysaassshSS.saassshSS(c,addr,cusname)
		elif int(ch)==2:
			c.sendall( " You have selected INFRASTRUCURE AS A SERVICE " )
		elif int(ch)==3:
			c.sendall( " You have selected STORAGE AS A SERVICE " )
			piystaasSS.staasSS(c,addr,cusname)	       
		elif int(ch)==4:
			c.sendall( " You have selected DATABASE AS A SERVICE ")
		elif int(ch)==5:
			c.sendall( " You have selected PLATFORM AS A SERVICE ")
		elif int(ch)==6:
			c.sendall( """ Thanku Very Much For Using Our Services\n  
				  See You Soon\n                   """ )
		else:
			c.sendall( """ You have selected Wrong Choice 
			       Please Select Correct Choice """ )	     
                c.close()

#thread.start_new_thread(saassshSS ,(c,addr))


	

