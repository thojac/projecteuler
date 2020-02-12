from functools import reduce

def read_grid(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            line = line.split()
            matrix.append([int(i) for i in line])
    return matrix

def horisontal(row, col, dist, matrix):
    if col + dist <= len(matrix[row]):
        prod = reduce(lambda x, y: x * y, matrix[row][col:col+dist], 1)
        return {"row": row, "col": col, "dist": dist, "prod": prod, "type": "horisontal"}
    else:
        return {"row": row, "col": col, "dist": dist, "prod": 0, "type": "horisontal"}

def vertical(row, col, dist, matrix):
    if row + dist <= len(matrix):
        res = 1
        for index in range(row, row + dist):
            res *= matrix[index][col]
        return {"row": row, "col": col, "dist": dist, "prod": res, "type": "vertical"}
    else:
        return {"row": row, "col": col, "dist": dist, "prod": 0, "type": "vertical"}

def diagonal_right(row, col, dist, matrix):
    if row + dist <= len(matrix) and col + dist <= len(matrix[row]):
        prod = 1
        col_index = col
        for row_index in range(row, row + dist):
            for j in range(col_index, col_index+1):
                prod *= matrix[row_index][j]
                col_index += 1
        return {"row": row, "col": col, "dist": dist, "prod": prod, "type": "diagonal_right"}
    else:
        return {"row": row, "col": col, "dist": dist, "prod": 0, "type": "diagonal_right"}

def diagonal_left(row, col, dist, matrix):
    if col - dist >= -1 and row + dist <= len(matrix):
        prod = 1
        col_index = col
        for row_index in range(row, row + dist):
            prod *= matrix[row_index][col_index]
            col_index -= 1
        return {"row": row, "col": col, "dist": dist, "prod": prod, "type": "diagonal_left"}
    else:
        return {"row": row, "col": col, "dist": dist, "prod": 0, "type": "diagonal_left"}


def solution(dist, filename):
    matrix = read_grid(filename)

    horisontal_max = {"row": 0, "col": 0, "dist": 0, "prod": 0, "type": "horisontal"}
    vertical_max = {"row": 0, "col": 0, "dist": 0, "prod": 0, "type": "vertical"}
    diagonal_right_max = {"row": 0, "col": 0, "dist": 0, "prod": 0, "type": "diagonal_right"}
    diagonal_left_max = {"row": 0, "col": 0, "dist": 0, "prod": 0, "type": "diagonal_left"}

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            h = horisontal(row, col, dist, matrix)
            v = vertical(row, col, dist, matrix)
            dr = diagonal_right(row, col, dist, matrix)
            dl = diagonal_left(row, col, dist, matrix)

            if h["prod"] > horisontal_max["prod"]:
                horisontal_max = h
            if v["prod"] > vertical_max["prod"]:
                vertical_max = v
            if dr["prod"] > diagonal_right_max["prod"]:
                diagonal_right_max = dr
            if dl["prod"] > diagonal_left_max["prod"]:
                diagonal_left_max = dl

    print(horisontal_max)
    print(vertical_max)
    print(diagonal_right_max)
    print(diagonal_left_max)


if __name__ == "__main__":
    matrix = read_grid("grid.txt")
    print(solution(4, "grid.txt"))


