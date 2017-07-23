#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
count = 1
current_score = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, score = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        score = float(score)
	word = int(word)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
	current_score += score
    else:
        if current_count>99:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_word, current_count,current_score/current_count)
        current_count = 1
        current_word = word
	current_score = score

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s\t%s' % (current_word, current_count , current_score/current_count)

