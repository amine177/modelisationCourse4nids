# -*- coding: utf-8 -*-
# !/bin/env python
"""
    A program to illustrate the geometric law of probability
"""

import random
import sys


def test(p):
    """
        Returns 'S' if the random value is <= p
            else 'E'
    """

    r = random.random()
    return r <= p


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: ./geometric.py p')
        exit(1)

    try:
        p = float(sys.argv[1])
    except ValueError:
        print("No valid float was supplied.")
        exit(2)

    print("Working with: p = {:f}".format(p))
    print("Result: {:.1s}".format(test(p)))

    exit(0)
