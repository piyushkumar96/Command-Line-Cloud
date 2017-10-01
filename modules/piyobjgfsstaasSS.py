#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19934))

def objgfsstaasSS(c,addr,cusname):
		c.sendall(""" \n\t\t You have Choosen Gluster File System :\n
		                      \n THANKU YOU VERY MUCH Wait a Seconds:::::::::::\n\n
                             Please Enter The Size Of Drive You Want :   """)
		'''csize=c.recv(20)
		commands.getstatusoutput("lvcreate --size " + csize + "G --name p3  piycl")   #user folder create later in place of piyush
                print "lv1create"
		commands.getstatusoutput("mkfs.ext4 /dev/piycl/p3")
                print "lv1formate"
		commands.getstatusoutput("lvcreate --size " + csize + "G --name p2  piycl")   #user folder create later in place of piyush
                print "lv1create"
		commands.getstatusoutput("mkfs.ext4 /dev/piycl/p3")
                print "lv1formate"
		commands.getstatusoutput("mkdir -p /cloud/object/gfs/piyush3") #provide permission for write to user
                print "folder create"
		commands.getstatusoutput("mount /dev/piycl/p3  /cloud/object/gfs/piyush3")
                print "mounted"	
		fh=open("/etc/exports", mode="at")
		fh.write("/cloud/object/gfs/piyush3 *(rw,no_root_squash)" + "\n")
                fh.close()
                c.send("success")'''
		c.close()
