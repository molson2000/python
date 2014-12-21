#!/usr/bin/python
import os
ip = "8.8.8.8"
host = "ping -c 1 " + ip
if os.system(host) == 0:
	print "host is up"
else:
	print "host did not respond"

