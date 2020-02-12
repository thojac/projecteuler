#!/usr/bin/env python3

# Solution to Project Euler problem 81, 82 and 83, using dijkstra

from collections import defaultdict
import heapq
import numpy as np

SMALL_MATRIX = 'small_matrix.txt'
LARGE_MATRIX = 'large_matrix.txt'
UP, DOWN, LEFT, RIGHT = (-1,0), (1,0), (0,-1), (0,1)

def read_file(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            matrix.append([int(x) for x in line.split(',')])
    return np.asarray(matrix)

def get_neighbours(i, j, directions, matrix):
    neighbours = []
    for di, dj in directions:
        try:
            neighbours.append((matrix[i+di][j+dj], (i+di, j+dj)))
        except IndexError:
            continue
    return neighbours

# Matrix implementation of dijkstra
def dijkstra(matrix, source, target, directions):
    # Create data structures needed
    queue = [(matrix[source],source,())] # nodes need to process
    seen = set() # set (O(1) lookup) of seen nodes
    mins = {source: 0} # dict with min path dist from source
    
    if not isinstance(target, set):
        target = {target}
    
    while queue:
        # Pop node in queue with smallest cost
        cost, v1, path = heapq.heappop(queue) # num, (i, j), pathlist
        
        # Process it if not seen yet
        if v1 not in seen:
            seen.add(v1) # add as seen
            path = (v1, *path) # and update path
            
            # Finished if v1 is target
            if v1 in target: 
                return (cost, path)

            # If not, we need to process v1's neighbours
            for c, v2 in get_neighbours(*v1, directions, matrix):
                
                # Only process if not seen before
                if v2 not in seen:
                    
                    prev = mins.get(v2, None)
                    nextt = cost + c
                    
                    if prev is None or nextt < prev:
                        mins[v2] = nextt
                        heapq.heappush(queue, (nextt, v2, path))

    return (-1, ())

def solve_p81():
    matrix = read_file(LARGE_MATRIX)
    l = len(matrix) - 1
    return dijkstra(matrix, (0,0), (l,l), (RIGHT, DOWN))

def solve_p82():
    matrix = read_file(LARGE_MATRIX)
    l = len(matrix) - 1
    targets = {(idx,l) for idx in range(len(matrix))}
    return min([dijkstra(matrix, (idx,0), targets, (RIGHT, UP, DOWN)) for idx in range(len(matrix))])

def solve_p83():
    matrix = read_file(LARGE_MATRIX)
    l = len(matrix) - 1
    return dijkstra(matrix, (0,0), (l,l), (RIGHT, LEFT, UP, DOWN))

if __name__ == "__main__":
    print('p81\t', solve_p81()[0])
    print('p82\t', solve_p82()[0])
    print('p83\t',solve_p83()[0])
            