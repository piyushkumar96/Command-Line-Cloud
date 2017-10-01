#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys
import time

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19926))

def blkiscsistaasCS(s1,unamm):
		data8=s1.recv(3000)
                sys.stdout.write(data8)
                dsize=raw_input()
                s1.sendall(dsize)
		time.sleep(5)
		data9=s1.recv(3000)
		if data9=="success":
			time.sleep(10)
		        sys.stdout.write("\nRaw Hardisk is successfull mounted on your pc\n")
			q=commands.getstatusoutput("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.3 --discover") 
		        print q                                                   #later to discover iqn no and target  
			sys.stdout.write(" Enter 'login' keyword to login ")     
			logi=raw_input() 
			w=commands.getstatusoutput("iscsiadm --mode node --targetname my"+unamm+"iscsi --portal 192.168.1.3:3260 --"+logi) 
		                                 #general targetname  accorging to vgs  available later
			print w
		        sys.stdout.write(" you are loged in now you can use raw hardisk  :\n")
		        time.sleep(10)
		        sys.stdout.write(" If you want To logout then enter 'logout' :") 
		        logo=raw_input()
		        commands.getstatusoutput("iscsiadm --mode node --targetname my"+unamm+"iscsi --portal 192.168.1.3:3260 --"+logo) 
		                                 #general targetname  accorging to vgs  available later
		        sys.stdout.write(" you are loged out ::::::::::::::::::::::;\n\n\n\n  :")
                
                s1.close()

