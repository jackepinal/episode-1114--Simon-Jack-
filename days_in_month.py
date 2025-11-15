from is_leap_year import is_leap_year

def days_in_month(year: int, month: int) -> int:
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month >= 1 and month <= 7:
        if month % 2 == 1:
            return 31
        else:
            return 30
    elif month >= 8 and month <= 12:
        if month % 2 == 1:
            return 30
        else:
            return 31
    else:
        return 9999

if __name__ == '__main__':
# Test code.
    print(f'March 2023 should be 31: {days_in_month(2023, 3)}')
    print(f'August 1908 should be 31: {days_in_month(1908, 8)}')
    print(f'April 1999 should be 30: {days_in_month(1999, 4)}')
    print(f'February 2001 should be 28: {days_in_month(2001, 2)}')
    print(f'February 2016 should be 29: {days_in_month(2016, 2)}')