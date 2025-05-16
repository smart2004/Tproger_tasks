# написать код, который будет выдавать каждую последующую букву алфавита выводить столько раз, 
# какая он по счету

string = 'abcdefghijklmnopqrstuvwxyz'

multiplier = 1
updated = []
for letter in string:
    sum = letter * multiplier
    updated.append(sum)
    multiplier = multiplier + 1

for item in updated:
    print(item)

# print(*updated)
