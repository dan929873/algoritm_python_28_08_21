# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

m_max = 1000
m_min = -1000
numbers = 10

my_list = [random.randint(m_min, m_max) for i in range(numbers)]
print(my_list)

max_min = m_min

for i in my_list:
    if max_min < i and i < 0:
        max_min = i

print(my_list.index(max_min), max_min)
