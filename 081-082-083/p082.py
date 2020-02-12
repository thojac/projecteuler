#!/usr/bin/env python3

# Solution to Project Euler problem 82 using dijkstra, with premade edges

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

def create_edges(matrix):
    num_to_idx = {}
    idx_to_num = {}
    edges = []
    
    # Create a mapping from unique number to idx, and vice versa
    counter = 1
    for idx, x in enumerate(matrix):
        for idy, y in enumerate(x):
            num_to_idx[counter] = (idx, idy)
            idx_to_num[(idx,idy)] = counter
            counter += 1
    
    # Create all edges pointing to the right
    for i in range(len(matrix)):
        for j in range(len(matrix)-1):
            f = idx_to_num[i,j]
            t = idx_to_num[i,j+1]
            c = matrix[i,j+1]
            edges.append((f,t,c))
    
    # Create all edges pointing down
    for i in range(len(matrix) - 1):
        for j in range(1, len(matrix)-1):
            f = idx_to_num[i,j]
            t = idx_to_num[i+1,j]
            c = matrix[i+1,j]
            edges.append((f,t,c))
            
    # Create all edges pointing up
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)-1):
            f = idx_to_num[i,j]
            t = idx_to_num[i-1,j]
            c = matrix[i-1,j]
            edges.append((f,t,c))
            
    # And lastly create two extra edges for start and end:
    for i in range(len(matrix)):
        edges.append((0, idx_to_num[i, 0], matrix[i][0]))
        edges.append((idx_to_num[i,len(matrix)-1], -1, 0))
        
    return edges

# Graph implementation of dijkstra
def dijkstra_graph(edges, source, target):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    # Create data structures needed
    queue = [(0,source,())] # nodes need to process
    seen = set() # set (O(1) lookup) of seen nodes
    mins = {source: 0} # dict with min path dist from source
    
    while queue:
        # Pop node in queue with smallest cost
        cost, v1, path = heapq.heappop(queue) # num, (i, j), pathlist
        
        # Process it if not seen yet
        if v1 not in seen:
            seen.add(v1) # add as seen
            path = (v1, *path) # and update path
            
            # Finished if v1 is target
            if v1 == target: 
                return (cost, path)

            # If not, we need to process v1's neighbours
            for c, v2 in g.get(v1,None):
                
                # Only process if not seen before
                if v2 not in seen:
                    prev = mins.get(v2, None)
                    nextt = cost + c
                    
                    if prev is None or nextt < prev:
                        mins[v2] = nextt
                        heapq.heappush(queue, (nextt, v2, path))

    return (-1, ())

def solve():
    return dijkstra_graph(create_edges(read_file(LARGE_MATRIX)), 0, -1)[0]

if __name__ == "__main__":
    print(solve())
            