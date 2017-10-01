#!/usr/bin/python2

import socket
import commands
import thread
import string
import sys

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind(("", 19924))

def objgfsstaasCS(s1):
		data5=s1.recv(3000)
                sys.stdout.write(data5)
                s1.close()
