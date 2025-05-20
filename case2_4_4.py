# Дана некоторая строка:

# 'abcde'
# Переведите в верхний регистр все нечетные буквы этой строки. 
# В нашем случае должно получится следующее:

# 'AbCdE'

# Исходная строка
string = 'abcde'
result = ''

for index, char in enumerate(string):
    if index % 2 == 0:
        result += char.upper()
    else:
        result += char.lower()

# Выводим результат
print(result)
