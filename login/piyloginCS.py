#!/usr/bin/python2
import socket   #TCP
import commands
import sys   # for stdio.write
import getpass
import time
import piystartOSCS
import piyloginCS

#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 2002))
def loginCS(s1):
	dt41=s1.recv(1000)
	sys.stdout.write(dt41)
	unamm1=raw_input()                 # username for verfication
	s1.sendall(unamm1)
	dt51=s1.recv(1000)
	sys.stdout.write(dt51)
        paswd1=getpass.getpass()         # password for verification 
        s1.sendall(paswd1)
	print " \nWait a Second verification is taking place \n" 
        dt61=s1.recv(100)
	if dt61=="verified":
		piystartOSCS.startOSCS(s1,unamm1)
	else:
		print("\n\tUsername Or Password doesnot Match please type again !!!!!!!!\n ")
		time.sleep(3)
		piyloginCS.loginCS(s1)
	 	s1.close()
