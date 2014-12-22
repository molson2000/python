#!/usr/bin/python
import os
import hosts
host = "ping -c 1 " + hosts.servers
if os.system(host) == 0:
	print "host is up"
else:
	print "host did not respond!"

