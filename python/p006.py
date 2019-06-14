def sum_of_squares(n):
    return sum([i * i for i in range(1, n + 1)])

def square_of_sums(n):
    return pow(sum(range(1, n + 1)), 2)

def solution(n):
    return abs(sum_of_squares(n) - square_of_sums(n))

if __name__ == "__main__":
    print(solution(100))
