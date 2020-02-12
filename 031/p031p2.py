from itertools import combinations, chain, combinations_with_replacement
import time

# Problem  031 - Coin sums

# This is a subset sum problem

def multi_combinations(iterable, range_):
    comb = []
    for i in range_:
        for c in list(combinations(iterable, i)):
            comb.append(c)

    return comb

def coins_sums_dynamic():
    coin_set = (1, 2, 5, 10, 20, 50, 100)
    target_sum = 200


def coin_sums_brute_force():
    coin_set = (1, 2, 5, 10, 20, 50, 100, 200)
    target_sum = 200
    result = []

    for i in range(1, 21):
        for comb in combinations_with_replacement(coin_set, i):
            if sum(comb) == target_sum:
                result.append(comb)

    print(result[-1])

    return len(result)

# We use the standard dynamic programming algorithm to solve the subset sum problem over integers.
# The order of the coin values does not matter, but the values need to be unique.
def compute():
    TOTAL = 200

    # At the start of each loop iteration, ways[i] is the number of ways to use {any copies
    # of the all the coin values seen before this iteration} to form an unordered sum of i
    ways = [1] + [0] * TOTAL
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
            for i in range(len(ways) - coin):
                    ways[i + coin] += ways[i]
    return str(ways[-1])

def compute2(target, coins):
    if target == 0: return 1
    if len(coins) == 1: return not target % coins[0]

    return sum(compute2(new_target, coins[:-1]) for new_target in range(target, -1, -coins[-1]))


if __name__ == "__main__":
    print(coin_sums_brute_force())
    print(compute())
