#!/usr/bin/python
import sh

print "scanning..."

for num in range(7,10):
	address = "8.8.8." + str(num)

	try:
		sh.ping(address, "-c 1", _out="/dev/null")
		print "ping to", address, "OK"
	except sh.ErrorReturnCode_1:
		print "no reponse from", address
		
