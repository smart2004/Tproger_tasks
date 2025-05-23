# generate_stairs(5)

# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5


def generate_stairs(z):
#    arr = []
#    for step in range(0, z+1):
#        arr.append(step)

#        print(" ".join(arr))

    for step in range(1, z + 1):
        # Создаём строку из повторяющихся чисел с пробелами
        line = " ".join([str(step)] * step)
        print(line)


generate_stairs(5)
