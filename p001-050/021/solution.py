# Problem  021 - Amicable numbers


from lib import eulerlib

def d(n, factors=None):
    if not factors:
        factors = eulerlib.prime_factors(n)

    divisors = eulerlib.get_divisors(n, factors)
    return sum(divisors[:-1])


def solution(n):
    primes = eulerlib.generate_primes(n + 100)

    sum_ = 1
    for i in range(3, n):
        sum_ += d(i, eulerlib.prime_factors(i, primes))

    return sum_



if __name__ == "__main__":
    print(solution(10000))
