def sum_of_squares(n):
    res = 0
    for i in range(1, n + 1):
        res += (i * i)
    return res

def square_of_sums(n):
    res = sum(range(1, n + 1))
    return res * res

def solution(n):
    return abs(sum_of_squares(n) - square_of_sums(n))

if __name__ == "__main__":
    print(sum_of_squares(100))
    print(square_of_sums(100))
    print(solution(100))
