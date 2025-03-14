values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')

t = tuple(ints_as_strings)

l = list(ints_as_strings)

print(t)
print(l)
