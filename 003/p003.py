#!/usr/bin/env python3

# Solution to Project Euler problem 3

import math

def get_primes(limit):
    return [idx for idx,b in enumerate(sieve(limit)) if b]  

def sieve(limit):
    is_prime = [False, True] * ((limit // 2) + (limit % 2))
    is_prime[0], is_prime[1], is_prime[2] = False, False, True
    
    i = 3
    while i * i < limit:
        if is_prime[i]:
            for num in range(i*i, limit, i):
                is_prime[num] = False
        i += 2
    return is_prime

def get_factors(num):
    primes = get_primes(int(math.sqrt(num) + 1))
    factors = []
    
    for prime in primes:     
        while num % prime == 0:
            factors.append(prime)
            num //= prime
            
    return factors

def solve():
    return get_factors(600851475143)[-1]

if __name__ == "__main__":
    print(solve())
            