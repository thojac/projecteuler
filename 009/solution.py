def solution(wantedSum):
    lst = []

    for a in range(1, wantedSum // 3):
        b = a + 1
        c = wantedSum - (a + b)
        while  (a < b < c):
            if is_pythagorean_triplet(a, b, c):
                lst.append((a, b, c, a * b * c))

            # Increment values
            b += 1
            c -= 1

    return lst

def is_pythagorean_triplet(a, b, c):
    return (a < b < c) and (a * a) + (b * b) == (c * c)


if __name__ == "__main__":
    print(solution(1000))
