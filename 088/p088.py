#!/usr/bin/env python3

# Solution to Project Euler problem 88

def get_factors(number):
    all_factors = [(number,)]
    get_factors_rec(number, number, [], all_factors)
    return all_factors

def get_factors_rec(number, parent_value, parent_factors, all_factors):
    # Set new value to parent value, as this is the one we will transform
    new_value = parent_value
    
    # Loop through reversed
    for i in reversed(range(2, number)):
        
        if number % i == 0:
            # If new value larger than i, set it to i
            if new_value > i:
                new_value = i
                
            # If - we have a factor comb
            if number // i <= parent_value and i <= parent_value and number // i <= i:
                all_factors.append((*parent_factors, i, number // i))
                new_value = number // i
                
            # If need to look for more (recursively)
            if i <= parent_value:
                get_factors_rec(number // i, new_value, parent_factors[:] + [i], all_factors)
                
def calculate(factors, D, k_limit=(1 << 32)):
    for sett in factors:
        prodsum, k = get_product_sum_number(sett)
        if k >= 2 and k <= k_limit and ((k not in D) or (D[k] > prodsum)):
            D[k] = prodsum
        
def get_product_sum_number(sett):
    product = reduce(mul, sett)
    length = abs(sum(sett) - product) + len(sett)
    return product, length

def solve(k_limit, factor_limit): 
    factors = [get_factors(i) for i in range(factor_limit)]
    D = {}
    for i in range(2, factor_limit):
        calculate(factors[i], D, k_limit)
    return sum(set(D.values()))

if __name__ == "__main__":
    print(solve())
            