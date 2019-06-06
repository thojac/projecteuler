from math import factorial as fac

# Problem  015 - Lattice paths

# Solves by filling out sum of previous grids
def grid_solution(n):
    if n < 1: return 0

    # Init matrix
    matrix = [[0 for _ in range(n)] for i in range(n)]

    # Fill first row and col:
    fill_num = 2
    for i in range(0, n):
        matrix[0][i] = fill_num
        matrix[i][0] = fill_num
        fill_num += 1

    # Fill res of matrix based on first row and col
    for i in range(1, n):
        for j in range(1, n):
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

    return matrix[n-1][n-1]

# Solves by using binomial coefficient
def binom(n, k):
    return fac(n) // (fac(k) * fac(n - k))


if __name__ == "__main__":
    print(grid_solution(20))
    print(binom(40, 20))
