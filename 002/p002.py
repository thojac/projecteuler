#!/usr/bin/env python3

# Solution to Project Euler problem 2

def fibonacci(limit):
    seq = [1, 1]
    while (seq[-2] + seq[-1]) < limit:
        seq.append(seq[-2] + seq[-1])
    return seq

def solve():
    return sum(num for num in fibonacci(4000000) if num % 2)

if __name__ == "__main__":
    print(solve())
            