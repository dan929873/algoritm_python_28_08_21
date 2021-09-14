# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

n = 100     #максимальное число

my_list = [int(random.random()*n) for i in range(10)]
print(my_list)

def min_max_rev(list):
    min = n
    max = 0
    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i
    i_min = list.index(min)
    i_max = list.index(max)
    list[i_min], list[i_max] = list[i_max], list[i_min]

min_max_rev(my_list)
print(my_list)
