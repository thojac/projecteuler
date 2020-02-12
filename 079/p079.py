#!/usr/bin/env python3

# Solution to Project Euler problem 79

def read_file():
    keys = [list(str(int(line))) for line in open('keyring.txt')]
    for sublist in keys:
        for idx, item in enumerate(sublist):
            sublist[idx] = int(item)
    return keys

def solve_count(keylog):
    posmap = {i:[] for i in range(10)}
    averages = {i:(0,0) for i in range(10)} # avg, count

    # Count positions
    for sublst in keylog:
        for idx, item in enumerate(sublst):
            posmap[item].append(idx)

    # Calc averages        
    for key, lst in posmap.items():
        if lst:
            averages[key] = sum(lst) / len(lst), len(lst)

    # Sort averages
    averages = {k: v for k, v in sorted(averages.items(), key=lambda item: item[1])}

    # Find number based on this
    return int(''.join(map(str,[key for key, (avg, count) in averages.items() if count])))

def solve_DFS():
    pass

if __name__ == "__main__":
    print(solve_count(read_file()))
