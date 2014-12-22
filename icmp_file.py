#!/usr/bin/python
import os
from hosts import servers
host = "ping -c 1 " + hosts.servers
if os.system(host) == 0:
	print "host is up"
else:
	print "host did not respond"

