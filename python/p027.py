# Problem  027 - Quadratic primes

from eulerlib import sieve

def quadratic_formula(n):
    if n < 0 or n > 39: return -1
    return n**2 + n + 41

def generic_formula(n, a, b):
    return n**2 + (a * n) + b

def iterator():
    combinations = ((1, 1), (1, -1), (-1, 1), (-1, -1)) # test with diff combinations...
    for a in range(0, 1000):
        for b in range(0, 1001):
            for x, y in combinations:
                yield a*x , b*y

def solution():
    best_result = (0, 0, 0, 0) # (count, a, b, product)
    primes = sieve(20000) # True/False list, for fast lookup

    for a, b in iterator():
        n = 0
        while primes[generic_formula(n, a, b)]:
            n += 1
        if best_result[0] < n:
            best_result = (n, a, b, a* b)

    print(best_result)

if __name__ == "__main__":
    solution()

