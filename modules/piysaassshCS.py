#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import signal
import os
from functools import partial

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

s.bind(("", 19950))  # 0 for client


def signal_handler(unamm,signal,frame):
	while True:
		print "If want any more software (yes/no) "
		more=raw_input()
		if more=="yes":
			os.system("clear")
			sys.stdout.write('''
			\n\t\t We provide Following Software Services :
			\t\t 1. FireFox
			\t\t 2. Gnome-Terminal
			\t\t 3. Vlc
			\t\t 4. Wireshark
			\t\t 5. To go Back 
			\t\t 6. To Exit
			\nWhich Software you want Enter the name of software : ''')
			sw=raw_input()
	                if sw=="5":
	                	commands.getstatusoutput("python USER_MANUAL.py")
	                elif sw=="6":
	                        print"\n Thanku Very Much For using Our Services \n"
				sys.exit()
			else:	
				#signal.signal(2, partial(signal_handler, unamm))
				commands.getstatusoutput("ssh -X "+unamm+"@192.168.1.4"+" "+sw)
		else:
			print"\n Thanku Very Much For using Our Services \n"
			sys.exit()
		continue      
		s1.close()
		

def saassshCS(s1,unamm):
	while True:
		os.system("clear")
                data11=s1.recv(2000)
		sys.stdout.write(data11)
		sfwr=raw_input()   # software required 
		if sfwr=="5":
                	commands.getstatusoutput("python /root/Desktop/project/cloud/USER_MANNUAL.py")
                elif sfwr=="6":
                	print"\n Thanku Very Much For using Our Services \n"
			s1.close()
			sys.exit()
		else:
			s1.send(""+sfwr)
			data12=s1.recv(2000)  # wait a second
			print data12
			signal.signal(2, partial(signal_handler, unamm))
			commands.getstatusoutput("ssh -X "+unamm+"@192.168.1.4"+" "+sfwr)
	s1.close()


	

