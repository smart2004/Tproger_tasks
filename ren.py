julia = {1: 'ножницы', 
         2: 'расческа',
         3: 'фен',
         4: 'бигуди',
         5: 'плойка',
         6: 'машинка'}

julia_list = []
for i in julia.values():
    print(i)
    julia_list.append(i)

print(*julia_list)

print(julia_list[2], julia_list[5])
