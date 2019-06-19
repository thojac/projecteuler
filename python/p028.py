# Problem  028 - Number spiral diagonals

def get_layer_sum(side_len):
    if side_len == 1:
        return 1

    start = (side_len-2)**2 + (side_len - 1)
    end = side_len**2
    steps = side_len - 1

    return sum(list(range(start, end + 1, steps)))


# A bit more clever variant... Must start at 3 to work.
def get_layer_sum2(side_len):
    return (4 * (side_len**2)) - (6*(side_len - 1))

def get_spiral_diagonal_sum(limit):
    total_sum = 0
    for side_len in range(1, limit + 1, 2):
        total_sum += get_layer_sum(side_len)

    return total_sum


if __name__ == "__main__":
    print(get_spiral_diagonal_sum(5))
    print(get_spiral_diagonal_sum(1001))

