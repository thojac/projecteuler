# Problem  025 - 1000-digit Fibonacci number

def num_digits(n):
    return len(str(n))

def fib():
    i = 2
    f = 0
    f_pre1 = 1
    f_pre2 = 1
    while num_digits(f) < 1000:
        f = f_pre1 + f_pre2
        f_pre1, f_pre2 = f, f_pre1
        i += 1

    return (i, f)


if __name__ == "__main__":
    print(fib())
