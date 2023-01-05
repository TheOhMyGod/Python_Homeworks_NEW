import json
import os


def add_student(data):
    student_data[data[0]] = data[1:], {}

def add_score(last_name, lesson, score):
    if student_data.get(last_name) is None:
        print(f'Ученик {last_name} не найден.')
    else:
        if lesson in student_data[last_name][1]:
            student_data[last_name][1][lesson].extend(score)
        else:
            student_data[last_name][1][lesson] = score



def get_student(last_name):
    if student_data.get(last_name) is None:
        print(f'Ученик {last_name} не найден.')
    else:
        data = student_data[last_name]
        print(f'{last_name}{",".join(data[0])}:')
        print(*[f'{key}: {",".join(value)}' for key, value in data[1].items()], sep='\n')


def save_data():
        json.dump(student_data, open('student_data.json', 'w'))


def load_data():
    global student_data
    if os.stat('student_data.json').st_size == 0:
        student_data = {}
    else:
        student_data = json.load(open('student_data.json'))
