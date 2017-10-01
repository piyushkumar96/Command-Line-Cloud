#!/usr/bin/python2
import socket   #TCP
import commands
import sys   # for stdio.write
import getpass
import time
import piypassdMatch

#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19982))

def passdMatch():
	sys.stdout.write("\n Enter Your password :")
        uspaswd11=getpass.getpass()
        sys.stdout.write("\n ReEnter Your password :")
	uspaswd22=getpass.getpass()
	if "uspaswd11"=="uspaswd22":
		return (uspaswd22,"verified")					
	else:
		piypassdMatch.passdMatch()
	c.close()
