# /bin/evn python3
# -*- coding: utf-8 -*-


import sys
from scipy import integrate
import numpy as np


def compute_prob(f, a=-np.inf, b=np.inf):
    """Calculate integral with error correction"""

    res = integrate.quad(f, a, b)
    prec = 6
    prob = 0
    for i in res:
        prob -= round(i, prec)

    return -1 * prob


def expPDF(lam):
    """Create a probability density function"""

    def fn(x):
        return lam*np.exp(-lam*x)

    return fn


if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) != 4:
        print("Usage:\n calculate_probability.py lambda_value a b")
        sys.exit(1)

    else:
            print("P({} < X < {}) = {}".format(
                sys.argv[2], sys.argv[3],
                compute_prob(
                    expPDF(float(sys.argv[1])),
                    float(sys.argv[2]), float(sys.argv[3]))))
