# Дано число. Выведите в консоль количество четных цифр в этом числе.

figure = '23456789'

even = 0

for r in figure:
    if int(r) % 2 == 0:
        even += 1

print(even)
