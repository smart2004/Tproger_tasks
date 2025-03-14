# Make program to combine several dictionaries into one

a = {'A': 20, 'A1': 25}
b = {'B': 30}
c = {'C': 40}

# dict_ = {*a, *b, *c}
dict = {**a, **b, **c}

print(dict)
