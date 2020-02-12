#!/usr/bin/env python3

# Solution to Project Euler problem 4

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def solve():
    return max([i * j for i in range(900,1000) for j in range(900, 1000) if is_palindrome(i * j)])

if __name__ == "__main__":
    print(solve())
            