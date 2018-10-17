# !/bin/env python
# -*- coding: utf-8 -*-

# A script to plot a histogram of n tossess

import random
import matplotlib.pyplot as plt
import itertools


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


def plotHistogram(p, ti="X historgram", cl='b', la="Probability", n=3):
    """
        plotHistogram(p, ti, cl, la, n) plot a histogram of\n
        the random variable X : n H/T combinations -> P(X = x)\n
        p : probability of Head\n
        ti: title\n
        cl: color\n
        la: label\n
        n : number of tries
    """

    combinations = itertools.product('HF', repeat=n)
    y = []
    x = []
    hp = p
    tp = 1 - p
    for i in combinations:
        hc = i.count('H')
        if hc == 0:
            tc = len(i) - hc
            tot = tp ** tc
        elif hc < n:
            tc = len(i) - hc
            tot = hp ** hc * tp ** tc
        else:
            tot = hp ** hc

        if hc in x:
            y[x.index(hc)] += tot
        else:
            y.append(tot)
            x.append(hc)

    plt.scatter(x, y, label=la, color=cl)
    plt.title(ti)
    plt.xticks(x)
    plt.show()


if __name__ == "__main__":
    print("A single toss: {:s}".format(toss()))
    pd = ntoss(1000000, p=0.2)
    print("Porbabilites H: {:f}, T: {:f}"
          .format(pd['H'], pd['T']))
    plotHistogram(pd['H'], n=20)
