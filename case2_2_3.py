# №3 Дана строка. Удалите предпоследний символ из этой строки.

st = 'asdfghjkl'
q = st[-2]

new = []
for i in st:
    if i != q:
        new.append(i)
str_new = ''.join(new)

print(str_new)
