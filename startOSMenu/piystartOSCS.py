#!/usr/bin/python2
import socket   #TCP
import commands
import sys   # for stdio.write
import time
import piytyosREDHATCS
#import piytyosWINDOWSCS
#import piytyosMACOSCS
#import piytyosUbuntuCS
#import piytyosopenSUSECS
#import piytyosOthersCS

#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s1=socket.socket()
s1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s1.bind(("",2001))

def startOSCS(s1,unamm):
	while True:
		dt7=s1.recv(3000) 
		sys.stdout.write(dt7)
		choicee=raw_input()
		s1.send(""+choicee)
		if int(choicee)==1:
			piytyosREDHATCS.tyosREDHATCS(s1,unamm)
		elif int(choicee)==2:
			#piytyosWINDOWSCS.tyosWINDOWSCS(s1)
			pass
		elif int(choicee)==3:
			#piytyosMACOSCS.tyosMACOSCS(s1)
			pass
		elif int(choicee)==4:
			#piytyosUbuntuCS.tyosUbuntuCS(s1)
			pass
		elif int(choicee)==5:
			#piytyosopenSUSECS.tyosopenSUSECS(s1)
			pass
		elif int(choicee)==6:
			#piytyosOthersCS.tyosOthersCS(s1)
			pass
		elif int(choicee)==7:
			print"\n Thanku Very Much For using Our Services \n"
			s1.close()
			sys.exit()
		else:
		 	print ( """ You have selected Wrong Choice 
			       Please Select Correct Choice """ )
		s1.close()

