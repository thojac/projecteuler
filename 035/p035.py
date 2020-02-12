#!/usr/bin/env python3

# Solution to Project Euler problem 35

def sieve(n):
    is_prime = [1] * (n + 1)
    is_prime[0], is_prime[1] = 0, 0

    for i in range(2, int(math.sqrt(n) + 1)):
        if is_prime[i]:
            for j in range(i**2, n + 1, i):
                is_prime[j] = 0

    return is_prime

def generate_primes(n):
    return {index:index for index, i in enumerate(sieve(n)) if i}

def is_circular_prime(num, prime_dict):
    snum = str(num)
    for i in range(len(snum)):
        c = int(snum[i:] + snum[:i])
        if not c in prime_dict:
            return False
    return True

def solve():
    count = 0
    prime_dict = generate_primes(int(1e+6))
    for prime in prime_dict:
        count += 1 if is_circular_prime(prime, prime_dict) else 0
    return count

if __name__ == "__main__":
    print(solve())
            