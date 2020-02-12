#!/usr/bin/env python3

# Solution to Project Euler problem 33

from itertools import product
from functools import reduce
from fractions import Fraction
from operator import mul

def compare(num, den, c_num, c_den):
    try:
        return num/den == c_num/c_den and num % 10 != 0
    except ZeroDivisionError:
        return False

def check(num, den):
    ab = str(num)
    cd = str(den)
    res = []
    for i, j in product((0, 1), (0, 1)):
        if ab[i] == cd[j]:
            if compare(num, den, int(ab[-i+1]), int(cd[-j+1])):
                res.append((num, den))
    return res

def solve():
    res = []
    for num in range(10, 100):
        for den in range(num + 1, 100):
            res += check(num, den)
    
    return reduce(mul, [frac for frac in [Fraction(i, j) for i, j in res]]).denominator

if __name__ == "__main__":
    print(solve())
            