#!/usr/bin/python
import sh

host = "8.8.8.8"
if sh.ping("8.8.8.8", "-c 4") == 0:
	print "host is up"
else:
	print "No ping"
 
