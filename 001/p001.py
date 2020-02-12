# Factorize a numbers

def solution(end):
    res = {}
    for i in range(end + 1):
        factors = factorize(i)
        for key, value in factors.items():
            if res.get(key) and value > res[key]:
                res[key] = value
            elif not res.get(key):
                res[key] = value

    prod = 1
    for key, value in res.items():
        for i in range(value):
            prod *= key

    return prod


if __name__ == "__main__":
    res = solution(20)
    print(res)

