# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# a
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
# в том числе написанных самостоятельно.
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
import cProfile
import random
import math

# b
#------------------------------------------------------------------------------------
# def m_fun(s):
#     SIZE = s
#     mtx = [[random.randint(0,100)for _ in range(SIZE)] for _ in range(SIZE)]
#     max_min = - math.inf
#     for i in range(SIZE):
#         m_min = math.inf
#         for j in range(SIZE):
#             if m_min > mtx[j][i]:
#                 m_min = mtx[j][i]
#         if max_min < m_min:
#             max_min = m_min
#------------------------------------------------------------------------------------
# def m_fun2(s):
#     SIZE = s
#     mtx = [[random.randint(0,100)for _ in range(SIZE)] for _ in range(SIZE)]
#     # for line in mtx:
#     #     print(*line, sep = '\t')
#     max_min = min(mtx[0])
#     new_matrix = [[mtx[j][i] for j in range(len(mtx))] for i in range(len(mtx[0]) - 1, -1, -1)]
#
#     for i in range(SIZE):
#         if max_min < min(new_matrix[i]):
#             max_min = min(new_matrix[i])
#     # print(max_min)
#------------------------------------------------------------------------------------
# def minimum(l, val):
#   if not l[1:]:
#      return val
#   return minimum(l[1:], l[0] if l[0] < val else val)
#
# def m_fun3(SIZE):
#     mtx = [[random.randint(0,100)for _ in range(SIZE)] for _ in range(SIZE)]
#
#     min_max = - math.inf
#     new_matrix = [[mtx[j][i] for j in range(len(mtx))] for i in range(len(mtx[0]) - 1, -1, -1)]
#     for i in range(SIZE):
#         m = minimum(new_matrix[i], mtx[0][0])
#         if min_max < m:
#             min_max = m
#
#     # print(min_max)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# c
# Лидеры
# количество кода 2 вариант (применение min)
# вложенность 1 вариант (написанный на дз3)
# время выполнения 1 вариант (написанный на дз3)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

# d
# На всех вариантах подавался размер 100
#------------------------------------------------------------------------------------
# Вариант написанный на уроке без применения рекурсии и min max
# cProfile
# 52707 function calls in 0.017 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#     10000    0.006    0.000    0.013    0.000 random.py:172(randrange)
#     10000    0.003    0.000    0.016    0.000 random.py:216(randint)
#     10000    0.005    0.000    0.007    0.000 random.py:222(_randbelow)
#         1    0.001    0.001    0.019    0.019 task01.py:17(m_fun)
#         1    0.000    0.000    0.018    0.018 task01.py:19(<listcomp>)
#         1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12702    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#
# python -m timeit -n 1000 -s "ïmport task01" "task01.m_fun(100)"
#
# "task01.m_fun(100)" 100
# 1000 loops, best of 3: 11.4 msec per loop
#------------------------------------------------------------------------------------

# Вариант написанный с применением min()
# 52939 function calls in 0.017 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.020    0.020 <string>:1(<module>)
#     10000    0.006    0.000    0.013    0.000 random.py:172(randrange)
#     10000    0.003    0.000    0.016    0.000 random.py:216(randint)
#     10000    0.005    0.000    0.007    0.000 random.py:222(_randbelow)
#         1    0.000    0.000    0.020    0.020 task01.py:29(m_fun2)
#         1    0.000    0.000    0.019    0.019 task01.py:31(<listcomp>)
#         1    0.000    0.000    0.001    0.001 task01.py:35(<listcomp>)
#         1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#       101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       103    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12729    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#
# python -m timeit -n 1000 -s "ïmport task01" "task01.m_fun2(100)"
#
# "task01.m_fun2(100)"
# 1000 loops, best of 3: 11.9 msec per loop
#------------------------------------------------------------------------------------

#Вариант написанный с рекурсивной функцией
# 62839 function calls (52939 primitive calls) in 0.021 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#     10000    0.006    0.000    0.013    0.000 random.py:172(randrange)
#     10000    0.003    0.000    0.016    0.000 random.py:216(randint)
#     10000    0.005    0.000    0.007    0.000 random.py:222(_randbelow)
# 10000/100    0.005    0.000    0.005    0.000 task01.py:43(minimum)
#         1    0.000    0.000    0.024    0.024 task01.py:48(m_fun3)
#         1    0.000    0.000    0.018    0.018 task01.py:49(<listcomp>)
#         1    0.000    0.000    0.001    0.001 task01.py:52(<listcomp>)
#         1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#       101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12731    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#  "task01.m_fun3(100)"
# 1000 loops, best of 3: 16.2 msec per loop

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# Самым быстрым получился вариант без рекурсии и применения min(), рекурсия потратила много времени по обращению к функции и получилось большая вложенность
