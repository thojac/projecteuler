import datetime

# Problem  019 - Counting Sundays
# Note: datetime cheating...

def solution():
    sunday_count = 0
    for year in range(1901, 2000 + 1):
        # Loop through months
        for month in range(1, 12 + 1):
            if datetime.date(year, month, 1).weekday() == 6:
                sunday_count += 1

    return sunday_count

if __name__ == "__main__":
    print(solution())


