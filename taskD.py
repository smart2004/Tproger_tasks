# Make program to combine several dictionaries into one

a = {'A': 20, 'A1': 25}
b = {'B': 30}
c = {'C': 40}

dict = {}
for i in (a, b, c):
    dict.update(i)

print(dict)
