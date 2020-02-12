#!/usr/bin/env python3

# Solution to Project Euler problem 69

import math

def sieve(n):
    is_prime = [1] * (n + 1)
    is_prime[0], is_prime[1] = 0, 0

    for i in range(2, int(math.sqrt(n) + 1)):
        if is_prime[i]:
            for j in range(i**2, n + 1, i):
                is_prime[j] = 0

    return is_prime

def generate_primes(n):
    return [index for index, i in enumerate(sieve(n)) if i]

def prime_factors(n, primes=None):
    if not primes:
        primes = generate_primes(n)

    factors = []
    for prime in primes:
        if prime > math.sqrt(n): break

        count = 0
        while n % prime == 0:
            count += 1
            n = n // prime

        if count > 0:
            factors.append((prime, count))

    if n > 2:
        factors.append((n, 1))

    return factors

def phi(n, factors):
    x = factors[n]
    res = 1
    for prime, func in x[1]:
        res *= 1 - (1/prime)
    return int(res * n)

def solve():
    # Generate all primes up to 1m
    primes = generate_primes(1000000)

    # Generate list of factors for all numbers up to 1m
    factors = [(i, prime_factors(i, primes=primes)) for i in range(1000000)]

    index, maxnum = 0, 0
    for n in range(3, 1000000):
        res = n / phi(n, factors)
        if res > maxnum:
            index = n
            maxnum = res

    return index, maxnum
  


if __name__ == "__main__":
    print(solve())
