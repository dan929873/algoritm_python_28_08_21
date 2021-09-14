# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
# в том числе написанных самостоятельно.

import math

mtx = [[2, 33, 23], [45, 5, 67], [12, 55, 670]]


max_min = - math.inf
for i in mtx:
    m_min = math.inf
    for j in i:
        if m_min > j:
            m_min = j
    if max_min < m_min:
        max_min = m_min

print(max_min)
