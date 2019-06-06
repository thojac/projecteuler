# Problem  018 - Maximum path sum I
# Bruteforce - as problem 067 is same task, but not possible with brutefoce.

def parse_file(filename):
    triangle = []
    with open(filename) as file:
        for line in file:
            row = []
            for i in line.split():
                row.append(int(i))
            triangle.append(row)

    return triangle

def get_maximum_path_sum(triangle):
    return path_sum_rec(triangle, 0, 0)

def path_sum_rec(triangle, level, index):
    if level >= len(triangle): return 0

    left = path_sum_rec(triangle, level+1, index) + triangle[level][index]
    right = path_sum_rec(triangle, level+1, index+1) + triangle[level][index]

    return left if left > right else right


if __name__ == "__main__":
    triangle = parse_file("triangle_small.txt")
    print("small", get_maximum_path_sum(triangle))

    triangle = parse_file("triangle_medium.txt")
    print("medium", get_maximum_path_sum(triangle))
