# def sum_digits(num):
#    digits = [int(d) for d in str(num)]
#    return sum(digits)

# print(sum_digits(13579))

num = 13587
num_str = str(num)

total_sum = 0

for d in num_str:
    total_sum = total_sum + int(d)
    
print(total_sum)
