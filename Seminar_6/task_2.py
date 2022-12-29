my_list = [12, 'sadf', 5643]

digit_list = list(filter(lambda x: type(x) is not str, my_list))
word_list = list(filter(lambda x: type(x) is str, my_list))

print(digit_list)
print(word_list)
