#!/usr/bin/python

import sys, math
import Gene_Prediction
#import tokenize

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

j = int(0)
predictions = []
score = 0
while(j<g):
	line = FILE.readline().split()
	#if (dna_strand[line[0]:line[1]]):
	#	score+=line[2]	
	predictions = Gene_Prediction.Gene_Prediction(line[0], line[1], line[2])
	j+=1

if (DEBUG):
	print 'DEBUG: %r' % (DEBUG)
	print 'n: %g' % (n)
	print 'max_line_length: %g' % (max_line_length)
	print 'ceiling: %g' % (ceiling)
	print 'dna_strand: %r' % (dna_strand)
	print 'g: %g' % (g)
	print ''

print 'score: %g' % (score)
