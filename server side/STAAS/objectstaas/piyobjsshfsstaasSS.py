#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19933))

def objsshfsstaasSS(c,addr,cusname):
		c.sendall(""" \n\t\t You have Choosen SSH File System :\n
		                      \n THANKU YOU VERY MUCH Wait a Seconds:::::::::::\n\n
                             Please Enter The Size Of Drive You Want :   """)
		csize=c.recv(20)
		commands.getstatusoutput("lvcreate --size " + csize + "G --name "+cusname+"sshfs  piycl")   #user folder create later in place of piyush
                print "lvcreate"
		commands.getstatusoutput("mkfs.ext4 /dev/piycl/"+cusname+"sshfs")
                print "lvformate"
		commands.getstatusoutput("mkdir -p /cloud/object/sshfs/"+cusname+"sshfs") #provide permission for write to user
                print "folder create"
		commands.getstatusoutput("mount /dev/piycl/"+cusname+"sshfs  /cloud/object/sshfs/"+cusname+"sshfs")
		commands.getstatusoutput("systemctl restart sshd")
                print "mounted"	
                c.send("success")
                c.close()
