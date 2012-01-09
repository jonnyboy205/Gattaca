#!/usr/bin/python

import sys, math

DEBUG = True

max_line_length = float(80.0)

FILE = open(sys.argv[1] ,"r")

#read in first line
n = int(FILE.readline())
ceiling = math.ceil(n/max_line_length)

#read in next ceiling lines
i = int(0)
dna_strand = ''
while(i<ceiling):
	dna_strand += FILE.readline().strip()
	i+=1

g = int(FILE.readline())

if (DEBUG):
        print 'DEBUG: %r' % (DEBUG)
        print 'n: %g' % (n)
        print 'max_line_length: %g' % (max_line_length)
        print 'ceiling: %g' % (ceiling)
	print 'dna_strand: %r' % (dna_strand)
	print 'g: %g' % (g)

j = int(0)

