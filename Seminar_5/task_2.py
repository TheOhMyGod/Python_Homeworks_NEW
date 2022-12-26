board = list(range(1, 10))

def draw_board(board):
    """Отрисовка доски в терминале"""
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 13)

def player_input(player_token):
    """Игрок вводит свой ход"""
    valid = False
    while not valid:
        player_move = input(f'Поставьте ваш {player_token}! --> ')
        try:
            player_move = int(player_move)
        except:
            print('Вводите, пожалуйста, цифры от 1 до 9!')
            continue
        if player_move >= 1 and player_move <= 9:
            if(str(board[player_move - 1]) not in 'X0'):
                board[player_move - 1] = player_token
                valid = True
            else:
                print('Здесь уже стоит нолик')
        else:
            print('Здесь всего 9 клеток! Введите от 1 до 9 включительно!')

def check_win(board):
    """Проверка на выигрышную ситуацию"""
    win_cases = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    for cell in win_cases:
        if board[cell[0]] == board[cell[1]] == board[cell[2]]:
            return board[cell[0]]
        else:
            return False

def game(board):
    """Основной механизм игры"""
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            player_input('X')
        else:
            player_input('0')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'Выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_board(board)

game(board)
