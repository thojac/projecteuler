# Problem  026 - Reciprocal cycles

import string
from decimal import *
from eulerlib import boyer_moore

num_decimals = 1000
getcontext().prec = num_decimals

text = "ababababababbababbaabababbababbabab"
pattern = "abbabab"
alphabet = list(string.ascii_lowercase)

print(boyer_moore(text, pattern, alphabet))



def get_decimals_as_list(n):
    return [str(i) for i in tuple((Decimal(1) / Decimal(n)).as_tuple().digits)]

def get_distance_two_patterns(lst, p_len):
    if len(lst) < 2: return -1
    return (lst[1] - lst[0]) - p_len

def detect_longest_cycle(n, alphabet):
    text = get_decimals_as_list(n)
    print("text", text)
    if len(text) < 100: return -1 # no repeating patterns

    p_len = 1
    p_offset = 0

    pattern = [1,2,3]

    res = -1
    for i in range(4):
        # teste med 4 forsoek forst..
        pattern = text[p_offset:p_len + p_offset]
        matches = boyer_moore(text, pattern, alphabet)
        dist = get_distance_two_patterns(matches, p_len)
        if dist == -1: return -1
        if dist == 0:
            print("best pattern:", pattern)
            return len(pattern)
        p_len += dist

    return pattern


    """
    p_len = 5
    p_offset = 0
    print(text)
    print(pattern)

    res = boyer_moore(text, pattern, alphabet)
    print(res)
    dist = get_distance_two_patterns(res, p_len)
    print("dist", dist)
    p_len += 1
    pattern = text[p_offset:p_len + p_offset]
    print("pattern2", pattern)
    res = boyer_moore(text, pattern, alphabet)
    print("res2", res)
    """

def main():
    alphabet = [str(i) for i in range(0,10)]

    longest_pattern = (0, 0) # (n, longest)

    for n in range(1, 1000):
        print("TESTING ", n)
        length_pattern = detect_longest_cycle(str(n), alphabet)
        if length_pattern == -1:
            print(n, " no repeating pattern")
        if longest_pattern[1] < length_pattern:
            longest_pattern = (n, length_pattern)
        print("\n\n")

    print("longest_pattern", longest_pattern)





if __name__ == "__main__":
    main()

