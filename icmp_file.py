#!/usr/bin/python
import os
ip = import address
host = "ping -c 1 " + ip
if os.system(host) == 0:
	print "host is up"
else:
	print "host did not respond"

