# Дан словарь:

#{
#	'a': 1,
#	'b': 2,
#	'c': 3, 
#	'd': 4,
#}
# Получите список его значений:

#[1, 2, 3, 4]

dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    }

val = dic.values()

lst = []

for d in val:
    lst.append(d)
    
print(lst)
