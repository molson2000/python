#!/usr/bin/python
hobbits = ["frodo", "samwise", "gimly", "larry"]

for hobbit in hobbits:
    if hobbit == "gimly":
        print "gimly is a dwarf"
        break
    print "hello hobbitses, ", hobbit
else:
    print hobbit
