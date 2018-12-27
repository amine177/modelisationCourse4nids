# !/bin/env python
# -*- coding: utf-8 -*-


import sys


def Y(i=0, p=1/2):
    """returns a tuple representing E[Y] and V[Y]\n"""

    return (0, 1)


def Xt(t):
    """defines X as sum(Yi) i <= t\n"""

    x = []
    for i in range(t):
        x.append(Y(i))

    return x


def EX(X):
    """returns E[X] for X = sum(Yi) i <= t\n"""

    e = 0
    for x in X:
        e += x[0]

    return e


def VX(X):
    """returns V[X] for X = sum(Yi) i <= t\n"""

    v = 0
    for x in X:
        v += x[1]

    return v


if __name__ == "__main__":

    n = 100
    X = Xt(n)
    print("E[X_{}] = {}".format(n, EX(X)))
    print("V[X_{}] = {}".format(n, VX(X)))

    # don't trust the interpreter :P
    sys.exit(0)
