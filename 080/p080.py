#!/usr/bin/env python3

# Solution to Project Euler problem 80

from decimal import *
getcontext().prec = 102

def solve():
    summ = 0
    for num in range(100):
        dec = Decimal(num).sqrt().as_tuple().digits[:100]
        if len(dec) == 100:
            summ += sum(dec)
    return summ

if __name__ == "__main__":
    print(solve())
            