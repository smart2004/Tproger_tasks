# There are two lists, return list that cosists of elements from common lists
# from pandas import unique

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# unique_a = []
# unique_b = []

# for ai in a:
#    if ai not in unique_a:
#        unique_a.append(ai)

new_c = []

for i in a:
    for j in b:
        if i == j:
            if j not in new_c:
                new_c.append(j)
            
print(new_c)
