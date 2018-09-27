#!/bin/env python
# -*- coding: utf-8 -*-


# the class version

import sys
import random


p = float(sys.argv[1])
print("p="+str(p))
r = random.random()
print("r="+str(r))
if r <= p:
    print('S')
else:
    print('E')
