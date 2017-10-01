#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import piyblkstaasCS
import piyobjstaasCS
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19920))

def staasCS(s1,unamm):
                data2=s1.recv(3000)
                sys.stdout.write(data2)
		ch1=raw_input()
                s1.sendall(ch1)
		if  int(ch1) == 1:
			piyobjstaasCS.objstaasCS(s1,unamm)
		elif  int(ch1) == 2:
			piyblkstaasCS.blkstaasCS(s1,unamm)
		elif int(ch1) == 3:
			pass
		else:
			print( """ You have selected Wrong Choice 
			             Please Select Correct Choice """ )
                        #continue
		s1.close()

