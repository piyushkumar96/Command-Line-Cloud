#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import time

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19922))

def objnfsstaasCS(s1,unamm):
		data7=s1.recv(3000)
                sys.stdout.write(data7)
                
		lsize=raw_input()
		s1.send(lsize)
                time.sleep(10)
		status=s1.recv(20)
		if status == "success":
			commands.getstatusoutput("systemctl restart nfs")
			dname=raw_input("Enter your Drive Name  :")
			commands.getstatusoutput("mkdir /media/"+dname)
                        print "folder create"
			z=commands.getstatusoutput("mount 192.168.1.3:/cloud/object/nfs/"+unamm+"nfs  /media/"+dname)
		        print (z+"\n\n\n\n") # adding this mount point command
                        
                        print "mounted on desktop"                                                             # in /etc/fstab file
		else:
			pass
		s1.close()

