#!/usr/bin/env python

def aaCount(string):
	length = len(string)
	mCount = string.count("M")
	rCount = string.count("R")
	yCount = string.count("Y")
	lCount = string.count("L")
	x = string.replace("L","l",1000)
	totalCount = float(float(mCount + rCount + yCount + lCount) / float(length))
	return "Here is the modified string: " + x + "\n" + "Here is the number of M's: " +  str(mCount) + "\n" + "Here is the number of R's: " +  str(rCount) + "\n" + "Here is the number of Y's: " +  str(yCount) + "\n" + "Here is the number of L's: " +  str(lCount) + "\n" + "Here is the percentage of M's, R's, Y's and L's: " +  str(totalCount)



