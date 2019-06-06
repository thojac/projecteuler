def read_number(filename):
    number = []
    with open(filename) as file:
        for line in file:
            for n in line[:-1]:
                number.append(int(n))
    return number

def find_greatest_adjacent_product(n):
    """
    :param n: how many adjacent numbers
    :return: lst [index, sequence, product]
    """

    number = read_number("number.txt")
    largestProd = [0, [], 0]

    for index, _ in enumerate(number[:-n]):
        tempProd = [index, number[index:index+n], 1]
        for num in tempProd[1]:
            tempProd[2] *= num
        if tempProd[2] > largestProd[2]:
            largestProd = tempProd

    return largestProd


if __name__ == "__main__":
    print(find_greatest_adjacent_product(13))

