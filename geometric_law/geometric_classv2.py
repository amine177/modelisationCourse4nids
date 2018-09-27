#!/bin/env python
# -*- coding : utf-8 -*-


import sys
from random import random as r

epreuve = lambda p: r() <= p

x = 1
while not epreuve(float(sys.argv[1])):
    x += 1

print(x)
