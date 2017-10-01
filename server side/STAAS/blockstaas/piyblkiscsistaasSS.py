#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import time

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19936))

def blkiscsistaasSS(c,addr,cusname):
                c.sendall(""" \n\t\t You have Choosen Internet Small Computer System Interface File System :\n
		                      \n THANKU YOU VERY MUCH Wait a Seconds:::::::::::\n\n
                Please Enter The Size Of Drive You Want :   """)
		csize=c.recv(20)
		commands.getstatusoutput("lvcreate --size " + str(csize) + "G --name "+cusname+"iscsi  piycl")   #user folder create later in place of piyush         
                print "lvcreate"
		commands.getstatusoutput("touch /etc/tgt/conf.d/"+cusname+"iscsi.conf")   #user file create later in place of piyush
		fh=open("/etc/tgt/conf.d/"+cusname+"iscsi.conf", mode="at")
		fh.write("<target my"+cusname+"iscsi>\nbacking-store /dev/piycl/"+cusname+"iscsi \n</target>" + "\n")
                fh.close()
		commands.getstatusoutput("systemctl restart tgtd")
		#time.sleep(15)
                c.send("success")

