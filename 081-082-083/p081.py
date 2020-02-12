#!/usr/bin/env python3

# Solution to Project Euler problem 81

import numpy as np

def read_file(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            matrix.append([int(x) for x in line.split(',')])
    return np.asarray(matrix)

def find_min_path(matrix):
    cost_matrix = np.zeros(shape=(len(matrix), len(matrix)))
    cost_matrix[0][0] = matrix[0][0]
    
    # Start with finding cost of first row and first column
    for i in range(1,len(matrix)):
        cost_matrix[0][i] = cost_matrix[0][i-1] + matrix[0][i]
        cost_matrix[i][0] = cost_matrix[i-1][0] + matrix[i][0]
    
    # Then loop rest of the two matrixes...
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            cost_matrix[i][j] = min(cost_matrix[i-1][j], cost_matrix[i][j-1]) + matrix[i][j]
            
    return cost_matrix

def solve():
    matrix = read_file('p081_matrix.txt')
    return int(find_min_path(matrix)[-1][-1])

if __name__ == "__main__":
    print(solve())
            