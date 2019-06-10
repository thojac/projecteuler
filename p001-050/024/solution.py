# Problem  024 - Lexicographic permutations

import itertools

def get_nth_item(n, iterator):
    for i in range(n-1):
        next(iterator)

    return(next(iterator))

def solution():
    n = 1000000
    res = get_nth_item(n, itertools.permutations(range(0,10)))
    print(res)


if __name__ == "__main__":
    solution()
