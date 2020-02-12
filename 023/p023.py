# Problem  022 - Non-abundant sums
# all numbers greater than 28123, can be written as sum of two abundant numbers

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

def get_divisors(n, factors=None):
    if not factors:
        factors = prime_factors(n)

    divisors = [1]
    _divisors_rec(1, factors, divisors)
    divisors.sort()

    return divisors

def _divisors_rec(n, factors, divisors):
    for index, factor in enumerate(factors):
        x = factor[0] * n
        for _ in range(factor[1]):
            divisors.append(x)
            _divisors_rec(x, factors[(index + 1):], divisors)
            x *= factor[0]


def abundant_numbers(n):
    primes = generate_primes(n)
    abundant_num = []

    for i in range(12, n):
        divisors = get_divisors(i, prime_factors(i, primes))[:-1]
        sum_divisors = sum(divisors)

        if sum_divisors > i:
            abundant_num.append(i)

    return abundant_num

def solution():
    n = 28124
    abundant_num = abundant_numbers(n)
    comb = [1] * (n + 1)

    for index, x in enumerate(abundant_num[:-1]):
        for y in abundant_num[index:]:
            if (x + y) > n: break
            else: comb[x+y] = 0

    return sum(index for index, i in enumerate(comb) if i)

if __name__ == "__main__":
    print(solution())
