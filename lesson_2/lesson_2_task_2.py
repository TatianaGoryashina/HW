def is_year_leap(year_to_check):
    if year_to_check % 4 == 0:
        return True
    else:
        return False


year_to_check = input("Введите год: ")
year_to_check = int(year_to_check)
result = is_year_leap(year_to_check)


print(f"год {year_to_check}: {result}")
