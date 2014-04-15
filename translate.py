#!/usr/bin/env python
'''
Write a script “translate.py” that asks the user for some input with the following prompt: Enter
some text:

'''

dataRequest = raw_input("Enter some text: ")
dataRequest = dataRequest.replace('a', '4')
dataRequest = dataRequest.replace('b', '8')
dataRequest = dataRequest.replace('e', '3')
dataRequest = dataRequest.replace('l', '1')
dataRequest = dataRequest.replace('o', '0')
dataRequest = dataRequest.replace('s', '5')
dataRequest = dataRequest.replace('t', '7')
print dataRequest