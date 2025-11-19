def month_to_season(season):
    if season in (1, 2, 12):
        print('Зима')
    elif season in (3, 4, 5):
        print('Весна')
    elif season in (6, 7, 8):
        print('Лето')
    elif season in (9, 10, 11):
        print('Осень')


month_to_season(115)
