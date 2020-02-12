#!/usr/bin/env python3

# Solution to Project Euler problem 39

from itertools import combinations
import operator

def is_right_angle(a, b, c):
    return (a**2 + b**2) == c**2

def solve():
    # Creates a simple dict to keep data
    D = {i:0 for i in range(1, 1000 + 1)}
    perimeter = 1000

    # Collects every combination with p <= 1000
    for comb in combinations(range(1, perimeter + 1), 3):
        if sum(comb) <= perimeter and is_right_angle(*comb):
            D[sum(comb)] += 1

    # Find which perimeter resultet in most possible combinations
    return max(D.items(), key=operator.itemgetter(1))


if __name__ == "__main__":
    print(solve())
            