my_list = list(input('Введите числа / слова и другие символы через пробел:\n'))
print(my_list)
print('\n')

for i in range(len(my_list) - 1):
    if my_list[i] == ' ':
        continue
    else:
        for j in range(len(my_list) - 1):
            if i + 1 + j < len(my_list):
                if my_list[i + 1 + j] != ' ':
                    my_list[i] += my_list[i + 1 + j]
                    my_list[i + 1 + j] = ' '
                else:
                    break
            else:
                break

print(my_list)
print('\n')

count_spaces = my_list.count(' ')

for i in range(count_spaces):
    my_list.remove(' ')

print(my_list)
print('\n')

count_el = len(my_list)

if count_el % 2 == 0:
    for i in range(len(my_list)):
        if i % 2 == 0:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
else:
    for i in range(len(my_list) - 1):
        if i % 2 == 0:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


print(my_list)


