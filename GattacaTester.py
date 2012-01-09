#!/usr/bin/python

import sys, math

DEBUG = True

max_line_length = float(80.0)

FILE = open(sys.argv[1] ,"r")

#read in first line
first_line = float(FILE.readline())
ceiling = math.ceil(first_line/max_line_length)

if (DEBUG):
	print 'DEBUG: %r' % (DEBUG)
	print 'first_line: %g' % (first_line)
	print 'max_line_length: %g' % (max_line_length)
	print 'ceiling: %g' % (ceiling)


