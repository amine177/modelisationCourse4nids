# !/bin/env python
# -*- coding: utf-8 -*-

import random


def toss(p=0.5):
    """
        toss(p) toss a coin\n
        returns 'H' if random.random < p (0.5 by default) else 'T'
    """

    r = random.random()
    return 'H' if r < p else 'T'


def ntoss(n, p=0.5):
    """
        ntoss(n, p) tosses a coin n times\n
        return a dict {'H': P('H'), 'T': P('T')}\n
        relies on toss(p)
    """

    hs = 0
    for i in range(n):
        if toss(p) == 'H':
            hs += 1

    return {'H': hs / n, 'T': (n-hs) / n}


if __name__ == "__main__":
    print("A single toss: {:s}".format(toss()))
    pd = ntoss(1000000)
    print("Porbabilites H: {:f}, T: {:f}"
          .format(pd['H'], pd['T']))
