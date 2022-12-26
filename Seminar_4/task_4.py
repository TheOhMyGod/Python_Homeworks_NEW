my_list = [7, 5, 3, 3, 2]

number = int(input('Введите рейтинг:\n'))
print(my_list)
print()

for i in range(len(my_list)):
    if my_list[i] == number and my_list[i + 1] < number:
        my_list.insert(i + 1, number)
        break
    else:
        if my_list[i] < number:
            my_list.insert(i, number)
            break

print(my_list)