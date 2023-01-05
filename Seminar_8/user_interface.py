import data

def see_result(last_name):
    data.get_student(last_name)

def add_student():
    surname = input("Введите Фамилию: ")
    name = input("Введите имя: ")
    group = input("Введите класс: ")
    data.add_student([surname, name, group])


def add_score():
    last_name = input("Введите фамилию ученика: ")
    subject = input("Введите предмет: ")
    score = input("Введите оценку или оценки через пробел: ").split()
    data.add_score(last_name, subject, score)
