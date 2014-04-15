#!/usr/bin/env python

shortString = "Hello \
There"
doubleQuotes = 'hello "My love"'

longString = """Hello Sir, \
how is it going?"""
myString = "Praise"
myString = "f" + myString[1:]

myNumber = "2"

print longString.find('z')
print myNumber + myNumber
print myNumber * 3
print int(myNumber)
print float(myNumber)
print shortString
print longString
print doubleQuotes
print len(longString)
print longString[2:7]
print myString.upper()

email = raw_input("Whats your email? ")
emailCheck = email.find("@")
if emailCheck == True:
    print "Passed, valid email";
else:
    print "Sorry, enter valid email"

    