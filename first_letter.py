#!/usr/bin/env python

passwd = raw_input("Tell me your passwd: ")
getFirstLetter = passwd[0]
print getFirstLetter.upper()

'''
Using the format method
'''

name = raw_input("Enter your name: ")
numHeads = raw_input("Number of heads: ")
numArms = raw_input("Number of arms: ")

# Below code takes the first letter, capitalises it and puts it back in the string.
name = name[0].upper() + name[1:]

print "{} has {} heads and {} arms".format(name,numHeads,numArms)