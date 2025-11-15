import sys
from is_valid_date import is_valid_date

def day_counter(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    # Flip the dates if needed.
    if year2 < year1 or (year2 == year1 and month2 < month1) or (year2 == year1 and month2 == month1 and day2 < day1):
        return day_counter(year2, month2, day2, year1, month1, day1)

    current_day = day1
    current_month = month1
    current_year = year1

    target_day = day2
    target_month = month2
    target_year = year2

    day_count = 0

    # Look up DeMorgan’s Law.
    while current_day != target_day or current_month != target_month or current_year != target_year:
        current_day += 1
        day_count += 1

        if not is_valid_date(current_year, current_month, current_day):
            current_month += 1
            current_day = 1

            if not is_valid_date(current_year, current_month, current_day):
                current_month = 1
                current_year += 1

    return day_count


if __name__ == '__main__':
    if len(sys.argv) < 7:
        print('Usage: day_counter.py <year1> <month1> <day1> <year2> <month2> <day2>')
    else:
        year1 = int(sys.argv[1])
        month1 = int(sys.argv[2])
        day1 = int(sys.argv[3])
        year2 = int(sys.argv[4])
        month2 = int(sys.argv[5])
        day2 = int(sys.argv[6])

        print(f'There are {day_counter(year1, month1, day1, year2, month2, day2)} days between {year1}-{month1}-{day1} and {year2}-{month2}-{day2}.')
        #some more awesome codeg