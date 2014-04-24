#!/usr/bin/env python
from __future__ import division
from random import randint

heads = 0
tails = 0

for trial in range(0,10000):
    while randint(0,1) == 0:
        tails += 1
    heads += 1
print "Heads:", heads
print "Tails:", tails
print "heads / tails = ", heads/tails