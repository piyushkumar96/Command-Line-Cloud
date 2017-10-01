#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import time
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 1995))

def saassshSS(c,addr,cusname):
	while True:
		c.sendall(""" \n\t\t We provide Following Software Services :
		\t\t 1. FireFox
		\t\t 2. Gnome-Terminal
		\t\t 3. Vlc
		\t\t 4. Wireshark
		\t\t 5. To go Back
		\t\t 6. To Exit
		\nWhich Software you want Enter the name of software : """)
		time.sleep(1)
		sfwr=string.lower(c.recv(20).strip())  
		if sfwr=="5":
			pass
		elif sfwr=="6":
			print"\n Session Terminated of client "+cusname+" \n"
			c.close()
		else:
			c.send(" You want "+sfwr+"  Wait a Second ")		     
                c.close()

#thread.start_new_thread(saassshSS ,(c,addr))


	

