#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19923))

def objsshfsstaasCS(s1,unamm):
		data8=s1.recv(3000)
                sys.stdout.write(data8)
                
		slsize=raw_input()
		s1.send(slsize)

		status=s1.recv(20)
		if status == "success":
			dname=raw_input("Enter your Drive Name  :")
			commands.getstatusoutput("mkdir /media/" + dname)
                        print "folder created"
			commands.getstatusoutput("sshfs 192.168.1.3:/cloud/object/sshfs/"+unamm+"sshfs  /media/"+dname) #for other users
                        print "mounted on desktop"                    # adding this mount point command  in /etc/fstab file
		else:
			pass
		s1.close()
