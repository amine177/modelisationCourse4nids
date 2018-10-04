# -*- coding: utf-8 -*-
# !/bin/env python
"""
    A program to illustrate the geometric law of probability
"""

import random
import sys


def test(p):
    """
        Returns True if the random value is <= p
            else False
    """

    r = random.random()
    return r <= p


def geom(p):

    x = 1
    while not test(p):
        x += 1

    return x


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: ./geometric.py p repeat')
        exit(1)

    try:
        p = float(sys.argv[1])
        rep = int(sys.argv[2])

    except ValueError:
        print("No valid float was supplied.")
        exit(2)

    s = 0
    for i in range(rep):
        s += geom(p)

    print("The mean of the success rate is {:f}"
          .format(s / rep))
    exit(0)
