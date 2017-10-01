#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19932))

def objnfsstaasSS(c,addr,cusname):
		c.sendall(""" \n\t\t You have Choosen Network File System :\n
		                      \n THANKU YOU VERY MUCH Wait a Seconds:::::::::::\n\n
                             Please Enter The Size Of Drive You Want :   """)
		csize=c.recv(20)
		commands.getstatusoutput("lvcreate --size " + csize + "G --name "+cusname+"nfs  piycl")   #user folder create later in place of piyush
                print "lvcreate"
		commands.getstatusoutput("mkfs.ext4 /dev/piycl/"+cusname+"nfs")
                print "lvformate"
		commands.getstatusoutput("mkdir -p /cloud/object/nfs/"+cusname+"nfs") #provide permission for write to user
                print "folder create"
		commands.getstatusoutput("mount /dev/piycl/"+cusname+"nfs  /cloud/object/nfs/"+cusname+"nfs")             
                print "mounted"	
		fh=open("/etc/exports", mode="at")
		fh.write("/cloud/object/nfs/"+cusname+"nfs *(rw,no_root_squash)" + "\n")
                fh.close()
		commands.getstatusoutput("systemctl restart nfs-server")
                c.send("success")
		c.close()

