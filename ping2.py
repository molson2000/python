#!/usr/bin/python
import sh

host = "192.168.50.141"
if sh.ping(host) == 0:
	print "host ", host, "  is up"
else:
	print "No ping"
 
