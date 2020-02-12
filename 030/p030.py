# Problem  030 - Distinct powers

def solution():
    res = []
    for num in range(2, 1000000):
        digit_sum = sum(int(n)**5 for n in str(num))
        if num == digit_sum:
            res.append(num)
    return (res, sum(res))

if __name__ == "__main__":
    solution()
