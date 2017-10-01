#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piyobjnfsstaasCS
import piyobjsshfsstaasCS
import piyobjgfsstaasCS

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19921))

def objstaasCS(s1,unamm):
	while True:
	        data3=s1.recv(3000)
                sys.stdout.write(data3)
		obtype1=raw_input()
                s1.send(obtype1)
                print "choice "+obtype1
	        if  int(obtype1) == 1:
			piyobjnfsstaasCS.objnfsstaasCS(s1,unamm)
		elif  int(obtype1) == 2:
		        piyobjsshfsstaasCS.objsshfsstaasCS(s1,unamm)
                elif  int(obtype1) == 3:
		        piyobjgfsstaasCS.objgfsstaasCS(s1,unamm)
 		elif int(obtype1) == 4:
                        break
 		else:
 		     s1.send( """ You have selected Wrong Choice 
		       Please Select Correct Choice """ )
                     continue
                s1.close()

