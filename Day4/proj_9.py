def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

while True:
    year_to_check = input("Enter a year: ")
    if year_to_check.isdigit():
        year_to_check = int(year_to_check)
    else:
        print('Enter a valid year')
        continue
    if is_leap_year(year_to_check):
        print(f"{year_to_check} is a leap year.")
        break
    else:
        print(f"{year_to_check} is not a leap year.")
    break