l1 = [1, 3, 6, 8, 0]
l2 = [3, 4, 6, 9, 0]

new_l = []

for d in l1:
    if d not in l2:
        new_l.append(d)

print(new_l)
