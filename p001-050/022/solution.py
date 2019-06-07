# Problem  022 - Names scores

import string

def parse_file(filename):
    with open(filename) as file:
        res = file.readline().replace('"', '').split(",")

    return res

def letter_value(letter):
    return string.ascii_uppercase.index(letter) + 1

def name_value(name):
    return sum([letter_value(letter) for letter in name])


def solution():
    name_list = parse_file("p022_names.txt")
    name_list.sort()

    sum_ = 0
    for index, name in enumerate(name_list):
        sum_ += name_value(name) * (index + 1)

    return sum_

if __name__ == "__main__":
    print(solution())
