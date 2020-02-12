#!/usr/bin/env python3

# Solution to Project Euler problem 34

import math

def is_curious_number(num):
    return sum([math.factorial(int(x)) for x in str(num)]) == num

def solve():
    return sum((num for num in range(3, 100000) if is_curious_number(num)))

if __name__ == "__main__":
    print(solve())
            