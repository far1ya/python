def days_in_month(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return "Invalid month"

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))
print(f"The number of days in month {month} of year {year} is: {days_in_month(month, year)}")
