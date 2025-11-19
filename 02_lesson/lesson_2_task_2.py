def is_year_leap(year):
    if (year % 4) == 0:
        leap = True
    else:
        leap = False
    print('год ', year, ':', leap)


is_year_leap(2021)
