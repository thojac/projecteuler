def parse_file(filename):
    matrix = [[] for i in range(50)] # 50 lists

    with open(filename) as file:
        for line in file:
            for lst, item in zip(matrix, list(line)):
                lst.append(int(item))

    return matrix[40:] # only return last 10 lines

def run():
    lst = parse_file("numbers.txt")

    print(lst)

if __name__ == "__main__":
    run()
