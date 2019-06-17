# Problem  026 - Reciprocal cycles

from eulerlib import generate_primes

"""
Note: This task could be solved faster by looping over a list of all
cyclic prime numbers. But then cycle_length would be easier to write,
and i would have to manually create a list containing them
"""


def is_cyclic_prime(prime):
    for n in str(prime):
        if n in ['0', '2', '4', '5', '6', '8']:
            return False
    return True

def is_full_reptend_prime(p):
    k = p - 1
    print(p, '\t', 10**k, 10**k / p, "==", 1 % p)
    return 10**k == 1


def generate_decimals_iterator_2(n):
    for i in iter(int, 1):
        yield 10**i % n


def generate_decimal_iterator(denominator):
    numerator = 10
    while numerator != 0:
        yield numerator // denominator
        numerator = (numerator % denominator) * 10

# Not working on quite a few numbers
def _cycle_length(n):
    iter_decimal = generate_decimal_iterator(n)

    # skip first, as this is often 1 - aka terminating cond
    count = -1
    prev = -1
    for dec in iter_decimal:
        count += 1
        #print("dec:\t\t", dec)
        if (dec == 1 or dec == 0) and count > 1:
            return count
        elif prev == dec:
            # Same num inf
            return 1
        prev = dec

    # iterator finished- without reaching repeating patter
    return 0


def solution():
    pass


if __name__ == "__main__":
    primes = generate_primes(20)
    cyclic_primes = list(filter(lambda x: is_full_reptend_prime(x), primes))
    print(primes)
    print(cyclic_primes)
