#!/bin/python3

import sys
import socket
from datetime import datetime

# Define Target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPV4
else:   
    print("Invalid amount of IP address")
    print("Syntax: Python3 scanner.py <IP>")

# Banner
print("-" * 50)
print("Scanning target "+ target) 
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,65535):
	  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) # Return error indicator
		print("Checking port {} ".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Host name could not be resolved")
	sys.exit()

except socket.error:
	print("Could not connect to server")
	sys.exit()
