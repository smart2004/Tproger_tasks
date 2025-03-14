# Exctract all elements less than 5 from the l list

l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newl = []

for i in l:
    if i < 5:
        newl.append(i)
        
print(newl)
