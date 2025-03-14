# It need to output first n strings of Pascal triangle/
def pascal_triangle(n):
    triangle = []  # make empty list

    for i in range(7):  # make cycle for pick elements from 0 to n
        row = [1]*(i+1)  # creates pyramyd through [1]
        for j in range(1, i):  # make double cycle for pick elements from 1 to i-1
#            row[j] = triangle[i-1][j-1]+triangle[i-1][j]  # equals sum for 2 elements from prev row
            prev_row = triangle[i-1]
            val1 = prev_row[j-1]
            val2 = prev_row[j]
            sum_val = val1 + val2
            row[j] = sum_val
        
        triangle.append(row)
    return triangle

def output_triangle(triangle):
    for row in triangle:
        print(''.join(map(str, row)).center(20))

n = 7
triangle = pascal_triangle(n)
print(triangle)


# Пример: предположим, что row = [1, 2, 3, 4, 5]

# 1. map(str, row)
# Функция map применяет функцию str к каждому элементу в iterable (в данном случае, 
# к каждому элементу списка row).
# Это преобразует каждый элемент списка row в строку.
# Например, если row = [1, 2, 3, 4, 5], то результат будет: ['1', '2', '3', '4', '5']

# 2. ''.join(...)
# Метод join объединяет все элементы, переданные ему в виде списка (или другого итерабельного объекта),
# в одну строку, вставляя между ними строку, на которой вызывается метод. 
# В данном случае это пустая строка ''.
# Таким образом, все строки из результата map будут объединены в одну строку без каких-либо разделителей.
# Например, результат будет: '12345'

# 3. .center(20)
# Метод center выравнивает строку по центру в поле шириной 20 символов.
# Если итоговая строка короче 20 символов, то слева и справа от строки будут добавлены пробелы,
# чтобы общая длина строки составила 20 символов. Если строка длиннее 20 символов, она останется неизменной.
# Например, если строка '12345' имеет длину 5, то результат будет: '      12345      '
# (5 пробелов слева и 5 пробелов справа).

# 4. print(...)
# Функция print выводит результат на экран. В данном случае это будет строка, выровненная по центру,
# содержащая элементы из row, объединенные в одну строку.

# В итоге, если row = [1, 2, 3, 4, 5], то на экране будет выведено:
# '      12345      '
