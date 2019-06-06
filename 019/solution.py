# Problem  019 - Counting Sundays

def get_days_in_month(month_num, year):
    if month_num == 2: return 29 if is_leap_year(year) else 28
    elif month_num in [4, 6, 9, 11]: return 30
    return 31

def is_leap_year(year):
    # Every 100 years, divisible by 100, but not 400 - not a leap year
    if year % 100 == 0:
        return (year % 400 == 0)

    # Else - if divisible by 4
    return year % 4 == 0

def get_days_in_year(year):
    return 366 if is_leap_year(year) else 365

def get_weekday(year, month, day):
    pass

def get_first_day_a_year(year, first_day):
    for curr_year in range(1901, year + 1):
        first_day = (first_day - (get_days_in_year(curr_year-1) % 7))
        if first_day < 1: first_day += 7
        print(curr_year, first_day)

    return first_day


def solution():
    # Loop from 1901 through 2000
    first_day = 7 # sunday
    for year in range(1901, 2000 + 1):
        # Loop through months
        first_day = get_first_day_a_year(year, first_day)
        for month in range(1, 12):
            for day in range(1, get_days_in_month(month, year)):
                pass

if __name__ == "__main__":

    get_first_day_a_year(1905, 7)

