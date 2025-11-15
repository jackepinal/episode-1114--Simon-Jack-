def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(f'2025: {is_leap_year(2025)}')
    print(f'2024: {is_leap_year(2024)}')
    print(f'1900: {is_leap_year(1900)}')
    print(f'2000: {is_leap_year(2000)}')
    print(f'2003: {is_leap_year(2003)}')