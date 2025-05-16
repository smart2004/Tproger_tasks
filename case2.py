list_numbers = [1, 2, 3, 4, 5, 6]

new_list = []

for n in list_numbers:
    new_list.append(n+n*0.1)

print(*new_list)
