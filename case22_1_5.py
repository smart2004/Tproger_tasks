# Дана некоторая строка:

# 'abcdeabc'
# Очистите ее от дублей символов:

# 'abcde'


# init_string = 'abcdeabc'
# list_init_string = list(init_string)

# sec_string = []

# for letter in list_init_string:
#    if letter != letter:
#        sec_string.append(letter)

# print(sec_string)


init_string = 'abcdeabc'
list_init_string = list(init_string)

sec_string = []

for letter in list_init_string:
    if letter not in sec_string:
        sec_string.append(letter)

print(sec_string)
