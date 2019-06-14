# Problem  014 - Longest Collatz sequence

def even(n):
    return n // 2

def odd(n):
    return (3 * n) + 1

def collatz_sequence(n):
    if n < 1: return 0

    counter = 1
    while n > 1:
        if n % 2 == 0: n = even(n)
        else: n = odd(n)
        counter += 1

    return counter

def longest_collatz_sequence():
    longest = (0, 0) # (num, counter)

    for i in range(1, 1000000):
        res = (i, collatz_sequence(i))
        if res[1] > longest[1]:
            longest = res

    return longest

if __name__ == "__main__":
    print(longest_collatz_sequence())
