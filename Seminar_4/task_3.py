words = input('Введите несколько слов через пробел:\n')
print()

words_list = words.split(' ')

for i in range(len(words_list)):
    print(f'{i + 1}. {words_list[i][:10]}')

