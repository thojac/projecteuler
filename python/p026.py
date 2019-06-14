# Problem  026 - Reciprocal cycles

import lib.eulerlib as eulerlib
from decimal import *

getcontext().prec = 50


def get_decimals_as_tuple(n):
    return (Decimal(1) / Decimal(n)).as_tuple()


def cycles():
    pass


if __name__ == "__main__":
    for i in range(1, 100):
        print(i, get_decimals_as_tuple(i).digits)
