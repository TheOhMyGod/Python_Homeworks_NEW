from random import randint


def input_candy(name):
    x = int(
        input(f'{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, введите корректное количество конфет: '))
    return x


def player_print(name, k, counter, value):
    print(
        f'Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.')


player_1 = input('Введите имя первого игрока: ')
player_2 = 'Робот Генадий'
candy = int(input('Введите количество конфет на столе: '))
flag = randint(0, 2)  # флаг очередности

if flag:
    print(f'Первый ходит {player_1}')
else:
    print(f'Первый ходит {player_2}')

counter_1 = 0
counter_2 = 0

while candy > 28:
    if flag:
        k = input_candy(player_1)
        counter_1 += k
        candy -= k
        flag = False
        player_print(player_1, k, counter_1, candy)
    else:
        k = randint(1, 29)
        counter_2 += k
        candy -= k
        flag = True
        player_print(player_2, k, counter_2, candy)

if flag:
    print(f'Выиграл {player_1}!')
else:
    print(f'Выиграл {player_2}!')