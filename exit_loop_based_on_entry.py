#!/usr/bin/env python
'''
Use a break statement to write a script that prompts the users for input repeatedly, only ending
when the user types “q” or “Q” to quit the program; a common way of creating an infinite loop
is to write “while True:”
'''

while True:
    receive = raw_input("Enter input: ")
    if receive == "q" or receive == "Q":
        print "You have successfully quit the application."
        break
    else:
        check += 1
