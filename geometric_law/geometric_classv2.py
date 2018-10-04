#!/bin/env python
# -*- coding : utf-8 -*-


import sys
from random import random as r

epreuve = lambda p: r() <= p


def geom(p):
    x = 1
    while not epreuve(float(sys.argv[1])):
        x += 1

    return x


p = float(sys.argv[1])
rep = 100
s = 0
for i in range(rep):
    s += geom(p)

print(s / rep)
