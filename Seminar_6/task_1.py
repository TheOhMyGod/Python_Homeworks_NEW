my_list = input('Введите несколько чисел через пробел:\n').split()
print(my_list)
print()

my_list = list(filter(lambda e: len(e) == 2, my_list))
print(my_list)