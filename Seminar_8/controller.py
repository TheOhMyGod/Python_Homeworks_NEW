import user_interface
from data import load_data, save_data
from user_interface import add_student, add_score, see_result


def controller():
    load_data()
    print('Выберите действие: \n1) Учитель\n2) Ученик\n3) Закончить работу')
    action = input()
    if action== '1':
        choice = 1
        while choice == 1:
            print(
            'Введите действие:\n'
            '1) Добавить ученика\n'
            '2) Добавить оценку\n'
            '3) Выйти в главное меню')
            action = input()
            if action == '1':
                add_student()
            if action == '2':
                add_score()
            if action == '3':
                choice = 0
        else:
            save_data()
            controller()
    elif action == '2':
        choice = 1
        while choice == 1:
            last_name = input('Чтобы посмотреть оценки ученика - введите его фамилию\n'
            'Для выхода в главное меню введите "0"\n')
            if last_name == '0':
                choice = 0
            else:
                see_result(last_name)
        controller()
    elif action == '3':
        print('Программа завершена!')
    else:
        print('Неверный ввод! Попробуйте еще раз.')
        controller()
