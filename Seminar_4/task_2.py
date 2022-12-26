month = int(input('Введите номер месяца:\n'))

year_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for k, v in year_dict.items():
    if month in year_dict[k]:
        print(k)