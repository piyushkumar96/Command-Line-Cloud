import socket
import commands
import thread
import sys
import time
import piytyosREDHATSS
#import piytyosWINDOWSSS
#import piytyosMACOSSS
#import piytyosUbuntuSS
#import piytyosopenSUSESS
#import piytyosOthersSS

#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 1997))
def startOSSS(c,addr,cusname):
	while True:
		c.sendall("""\n\t Which Type Of OS You Have From Following :
					      \t    1. REDHAT LINUX
					      \t    2. WINDOWS
					      \t    3. MAC OS X
					      \t    4. Ubuntu
					      \t    5. openSUSE
					      \t    6. Others
					      \t    7. To Exit
		   			      \t  Enter the Choice :""")
		choicei=c.recv(100) 
		if int(choicei)==1:
			piytyosREDHATSS.tyosREDHATSS(c,addr,cusname)
		elif int(choicei)==2:
			#piytyosWINDOWSSS.tyosWINDOWSSS(c,addr)
			pass
		elif int(choicei)==3:
			#piytyosMACOSSS.tyosMACOSSS(c,addr)
			pass
		elif int(choicei)==4:
			#piytyosUbuntuSS.tyosUbuntuSS(c,addr)
			pass
		elif int(choicei)==5:
			#piytyosopenSUSESS.tyosopenSUSESS(c,addr)
			pass
		elif int(choicei)==6:
			#piytyosOthersSS.tyosOthersSS(c,addr)
			pass
		elif int(choicei)==7:
			print"\n Thanku Very Much For using Our Services \n"
			c.close()
			sys.exit()
		else:
			print ( """ You have selected Wrong Choice 
		       		Please Select Correct Choice """ )
		c.close()		


