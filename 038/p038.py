#!/usr/bin/env python3

# Solution to Project Euler problem 38

def gen_concat_num(num, L):
    return int(''.join([str(num * x) for x in L]))

def is_pandigital(num):
    return sorted(str(num)) == [str(i) for i in range(1,10)]

def iter(L):
    k = 1
    largest = (0, 0, 0)
    while True:
        res = gen_concat_num(k, L)
        if len(str(res)) > 9:
            return largest
        elif len(str(res)) == 9:
            if is_pandigital(res) and res > largest[0]:
                largest = (res, k, L[::])
        k += 1
        
def solve():
    # k * (1,2,..n) --> k * [L]
    L = [1]
    largest = (0, 0, 0)
    for n in range(2, 10):
        L.append(n)
        res = iter(L)
        if res[0] > largest[0]:
            largest = res
    return largest

if __name__ == "__main__":
    print(solve())
            