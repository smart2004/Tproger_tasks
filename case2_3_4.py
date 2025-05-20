# Дана дата в следующем формате:

# '2025-12-31'
# Преобразуйте эту дату в следующий словарь:

date = '2025-12-31'

numbers = map(int, date.split('-'))

dic = {}

keys = ['year', 'month', 'day']
for key, n in zip(keys, numbers):
    dic[key] = str(n) 
