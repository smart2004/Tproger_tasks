# удалите элементы с заданным значением

lis = [1, 3, 5, 7, 8, 2, 6, 8, 6, 8]

# new = []

# for n in lis:
#    if n == 8:

lis = [l for l in lis if l != 8]

print(lis)
