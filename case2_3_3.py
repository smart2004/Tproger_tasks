# Даны числа, разделенные запятыми:

# '12,34,56'
# Найдите сумму этих чисел.

input_string = '12,34,56'

numbers = map(int, input_string.split(','))

for n in numbers:
    print(n)

total_sum = sum(numbers)

print(numbers)
print(total_sum)
