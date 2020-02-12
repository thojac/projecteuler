from itertools import combinations, chain

# Problem  031 - Coin sums

# This is a subset sum problem

def multi_combinations(iterable, range_):
    comb = []
    for i in range_:
        for c in list(combinations(iterable, i)):
            comb.append(c)

    return comb

def find_subset(lst, target):
    # Remove items in lst larger than target
    filtered_lst = filter(lambda x: x <= target, lst)

    # Create a list to place the result
    result = []

def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    sorted(final_list)
    return final_list

def hmm():
    X = [1, 2, 5, 10, 20, 50, 100]
    N = len(X)

    S = [0]
    for i in range(N):
        T = [X[i]+y for y in S]
        U = Union(T, S) # U is sorted by union function

        S = []
        y = U[0]
        S.append(y)
        for z in U:
            pass


# O(2^N * N)
def subset_sum_brute_force(iterable, curr_list, current_sum, target_sum, results):
    """
    args:
        iterable - items that should check if subset_sum of target_sum
        curr_list - tuple containing current numbers combined to find target_sum
        current_sum
        target_sum
        results - list containing sets with the final
    """

    for x in iterable:
        if current_sum + x == target_sum:
            results.append(curr_list[:] + [x])
        elif current_sum + x < target_sum:
            subset_sum_brute_force(iterable, curr_list[:] + [x], current_sum + x, target_sum, results)


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


def solution():
    subset = [1, 2, 5]
    target_sum = 10
    results = []

    subset_sum_brute_force(subset, [], 0, target_sum, results)
    for lst in results:
        print(lst)



def combinational_sum(iterable, target, result):
    for num in iterable:
        if target == num:
            result[0] += 1
        elif target > num:
            combinational_sum(iterable, target-num, result)

if __name__ == "__main__":
    solution()
