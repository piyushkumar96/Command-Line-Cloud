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
s.bind(("", 19981))

def UserDataStore(Fusname,Lusname,usname,uspaswd,emailid,mobileno):
	commands.getstatusoutput("useradd  "+usname)
	commands.getstatusoutput("echo "+uspaswd+" | passwd "+usname+" --stdin")
	fh=open("/root/Userinfo/user.py", mode="at")
	fh.write(Fusname+"-"+Lusname+":"+usname+":"+uspaswd+":"+emailid+":"+mobileno+"\n")
        fh.close()
	return 1  
