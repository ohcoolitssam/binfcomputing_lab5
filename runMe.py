#!/usr/bin/env python

from countAA import aaCount

file = open("aaInput.faa")
l = file.readlines()
lines = []
for i in range(0,len(l)):
	lines.append(l[i].rstrip())
lines = " ".join(lines)
print aaCount(lines)
