l = [234, 238, 239, 273, 254, 237, 233, 344, 543]

n = []

for c in l:
    if c == 237:
        break
    if c % 2 == 0:
        n.append(c)
        
print(n)
