# Выведите в консоль все числа в промежутке от 10 до 1000, 
# сумма первой и второй цифры которых равна пяти.

# gimme_five = []

# for s in range(9, 1000):
#    if len(str(s)) > 1:
#        if int(s[0]) + int(s[1]) == 5:
#            gimme_five.append(s)

# print(gimme_five)


# Выведите в консоль все числа в промежутке от 10 до 1000, 
# сумма первой и второй цифры которых равна пяти.

gimme_five = []

for s in range(1, 1001):
    string_s = str(s)
    if len(string_s) > 1:
        if int(string_s[0]) + int(string_s[1]) == 5:            
            gimme_five.append(s)
        
print(*gimme_five)
