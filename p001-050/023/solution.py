# Problem  022 - Non-abundant sums
# all numbers greater than 28123, can be written as sum of two abundant numbers

from lib import eulerlib

def abundant_numbers(n):
    primes = eulerlib.generate_primes(n)
    abundant_num = []

    for i in range(12, n):
        divisors = eulerlib.get_divisors(i, eulerlib.prime_factors(i, primes))[:-1]
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
