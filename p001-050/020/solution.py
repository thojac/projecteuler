# Problem  020 - Factorial digit sum

def fac(n):
    sum = 1
    while n > 1:
        sum *= n
        n -= 1
    return sum

def factorial_digit_sum(n):
    return sum(int(i) for i in list(str(fac(n))))

if __name__ == "__main__":
    print(factorial_digit_sum(100))
