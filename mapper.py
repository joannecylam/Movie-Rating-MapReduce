#!/usr/bin/env python


import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split(',')

	try:
		movieid=int(words[1])
	except ValueError:
		continue
	try:
		rating = float(words[2])
	except ValueError:
		continue
	print '%s\t%s' % (movieid, rating)
