#!/usr/bin/env python
'''
A test script to perform activities based on lenght of input. 
This goes the next step to include exceptions.
'''

try:
	holdWord = raw_input("Enter word: ")
	if len(holdWord) < 5:
		print "You entered less than 5 letter words."
	elif len(holdWord) == 5:
		print "You have entered a 5 letter word."
	else:
		print "you have entered more than 5 letter word."

except KeyboardInterrupt:
	print "You terminated the program rudely"
except:
	print "There is an error with your input."
