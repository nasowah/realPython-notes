#!/usr/bin/env python

# A while loop
n = 1
while (n <= 5):
    print "n =", n
    n = n + 1
print "loop finished"

# A for loop
for n in range(2,10):
    print "n =", n
print "Loop finished"

# A FOR loop within a for loop
for n in range (1,6):
    for j in ['a','b','c','d','e']:
        print "n =", n, "and j =", j
