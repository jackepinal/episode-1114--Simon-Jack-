from days_in_month import days_in_month

def is_valid_date(year: int, month: int, day: int) -> bool:
    if month < 1 or month > 12:
        return False

    if day < 1 or day > days_in_month(year, month):
        return False
    else:
        return True


if __name__ == '__main__':
    # Test code.
    print(f'2025-11-10 (True): {is_valid_date(2025, 11, 10)}')
    print(f'2027-11-32 (False): {is_valid_date(2027, 11, 32)}')
    print(f'2024-08-10 (True): {is_valid_date(2024, 8, 10)}')
    print(f'2024-02-29 (True): {is_valid_date(2024, 2, 29)}')
    print(f'2023-02-29 (False): {is_valid_date(2023, 2, 29)}')
    print(f'1900-02-29 (False): {is_valid_date(1900, 2, 29)}')
    print(f'2000-02-29 (True): {is_valid_date(2000, 2, 29)}')