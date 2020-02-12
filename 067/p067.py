#!/usr/bin/env python3

# Solution to Project Euler problem 67

from urllib.request import urlopen

def read_data():
    file = urlopen('https://projecteuler.net/project/resources/p067_triangle.txt')
    return [[int(i) for i in line.decode('utf-8').split()] for line in file] 

def solve():
    data = read_data()
    data.reverse()
#    for lower, upper in zip(data[1:], data()):
    for lower, upper in zip(reversed(data[1:]), reversed(data[:-1])):
        for left, right in zip(range(len(lower)-1), range(1, len(lower))):
            upper[left] += max(lower[left], lower[right])
    
    return data[-1][-1]


if __name__ == "__main__":
    print(solve())
            