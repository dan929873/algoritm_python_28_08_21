# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random

m_min = 0

my_list = [3,33,98,56,3,55,4]
print(my_list)

min1 = my_list[random.randint(m_min, len(my_list))]
min2 = my_list[random.randint(m_min, len(my_list))]
itr = 0
for i in my_list:
    if min1 > i:
        min1 = i
    if min2 > i and my_list.index(min1) != itr:
        min2 = i
    itr += 1
print(min1, min2)
