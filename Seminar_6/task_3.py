my_num = list(input('Введите любое число:\n'))

minus_dot = sum(([int(x) for x in my_num if x is not '.' and x is not ',']))

print(minus_dot)
