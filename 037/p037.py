#!/usr/bin/env python3

# Solution to Project Euler problem 37

# http://code.activestate.com/recipes/117119/
def gen_primes():
    prime_dict = {}
    num = 2
    while True:
        if num not in prime_dict:
            yield num
            prime_dict[num * num] = [num]
        else:
            for prime in prime_dict[num]:
                prime_dict.setdefault(prime + num, []).append(prime)
            del prime_dict[num]
        num += 1

def is_truncatable_prime(sprime, prime_dict, left_to_right=1):
    if not len(sprime):
        return True
    elif left_to_right:
        return int(sprime) in prime_dict and is_truncatable_prime(sprime[1:], prime_dict, left_to_right=1)
    else:
        return int(sprime) in prime_dict and is_truncatable_prime(sprime[:-1], prime_dict, left_to_right=0)

def solve():
    generator = gen_primes()
    prime_dict = {x:x for x in [next(generator) for _ in range(4)]} # skip 4 first primes
    res = []
    
    while len(res) < 11:
        prime = next(generator)
        prime_dict[prime] = prime # add to dict
        if is_truncatable_prime(str(prime), prime_dict, left_to_right=1) and is_truncatable_prime(str(prime), prime_dict, left_to_right=0):
            res.append(prime)
    return sum(res)

if __name__ == "__main__":
    print(solve())
            