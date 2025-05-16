# Дан кортеж с числами:

# (1, 2, 3, 4, 5)
# Найдите сумму элементов этого кортежа.

# tuple = (1, 2, 3, 4, 5)

# for i in tuple:
#    sum = i + i

# print(sum)

tuple_numbers = (1, 2, 3, 4, 5)
sum = 0

for i in tuple_numbers:
    sum = sum + i

print(sum)
