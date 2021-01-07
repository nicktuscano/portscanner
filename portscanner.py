#!/bin/python

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translates host to ipv4
else:
	print("Invalid argument.")
	print("Syntax: python3 portscanner.py <ip>")
	
#banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting scan.")
	sys.exit()

except socket.gaierror:
	print("host could not be resolved.")

except socket.error:
	print("Could not connect.")
	sys.exit()
