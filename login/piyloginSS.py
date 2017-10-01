#!/usr/bin/python2
import socket   #TCP
import commands
import sys   # for stdio.write
import getpass
import time
import piystartOSSS
import piyloginSS

#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 1998))

def loginSS(c,addr):
	c.sendall("Please Enter your Username :")
	cusname1=c.recv(100).strip()
	c.sendall("Please Enter your password :")
	cpasswd1=c.recv(100).strip()
	up1=commands.getstatusoutput("grep -w "+cusname1+"[:]"+cpasswd1+" /root/Userinfo/user.py")
	if up1[1]==cusname1+":"+cpasswd1 :
		c.send("verified") 
		time.sleep(2)
		piystartOSSS.startOSSS(c,addr,cusname1) 					
	else:
		c.sendall("notverified")
		time.sleep(2)
		piyloginSS.loginSS(c,addr)
	c.close()
