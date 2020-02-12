# Problem  016 - Power digit sum

def power_digit_sum(x, y):
    return sum(int(i) for i in list(str(pow(x,y))))

if __name__ == "__main__":
    print(power_digit_sum(2, 1000))
