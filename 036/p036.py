#!/usr/bin/env python3

# Solution to Project Euler problem 36

def is_palindrome(snum):
    return snum == snum[::-1]

def is_palindromic(num):
    return is_palindrome(bin(num)[2:]) and is_palindrome(str(num))

def solve():
    return sum([num for num in range(int(1e+6)) if is_palindromic(num)])

if __name__ == "__main__":
    print(solve())
            