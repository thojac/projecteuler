# Problem  026 - Reciprocal cycles

import string
from decimal import *

getcontext().prec = 50

text = "ababababababbababbaabababbababbabab"
pattern = "abbabab"
alphabet = list(string.ascii_lowercase)

print(boyer_moore(text, pattern, alphabet))



def get_decimals_as_tuple(n):
    return (Decimal(1) / Decimal(n)).as_tuple()


def cycles():
    pass


if __name__ == "__main__":
    pass
#    for i in range(1, 100):
#        print(i, get_decimals_as_tuple(i).digits)
