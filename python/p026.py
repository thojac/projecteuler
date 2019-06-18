# Problem  026 - Reciprocal cycles

"""
Note: This task could be solved faster by looping over a list of all
cyclic prime numbers. But then cycle_length would be easier to write
"""

def generate_decimal_iterator(denominator):
    numerator = 10
    while numerator != 0:
        yield numerator // denominator
        numerator = (numerator % denominator) * 10

# Now working on every possible number
def cycle_length_brute_force(n):
    last_position = {}

    position = 1
    dividend = 1
    while True:
        remainder = dividend % n

        if remainder == 0:
            return 0

        if remainder in last_position:
            return position - last_position[remainder]

        last_position[remainder] = position

        position += 1
        dividend = remainder * 10

def solution():
    max_n = (0, 0) # number, count
    for i in range(1, 1000):
        count = cycle_length_brute_force(i)
        if max_n[1] < count:
            max_n = (i, count)
    print(max_n)


if __name__ == "__main__":
    solution()
