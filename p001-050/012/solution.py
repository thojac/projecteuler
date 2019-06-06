from math import factorial as fac

def biom(n, r):
    return fac(n) // (fac(r) * fac(n - r))

def combinations(num_factors):
    return sum([biom(num_factors, r) for r in range(1, num_factors + 1)])

def get_triangle_num_based_on_divisors(lim):
    n = 1
    while True:
        triangle_num = get_triangle_num(n)
        num_divisors = get_divisors(triangle_num)
        if num_divisors > lim:
            return {"n": n, "triangle_num(n)": triangle_num, "num_divisors": num_divisors}
        n += 1

def get_triangle_num(n):
    return (n * (n + 1)) // 2

def get_divisors(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    return counter

def solution():
    print(get_triangle_num_based_on_divisors(500))


if __name__ == "__main__":
    solution()
