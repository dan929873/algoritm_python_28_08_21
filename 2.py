# Написать два алгоритма нахождения i-го по счёту простого числа.

import cProfile

#     Без использования "Решета Эратосфена";

def non_Era(n):

    lst = []
    for i in range(2, n+1):
        for j in lst:
            if i % j == 0:
                # если делитель найден, число не простое.
                break
        else:
            lst.append(i)
    print(lst)



# Решето "Эратосфена"

def Era(n):
    a = list(range(n+1))
    a[1] = 0
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    print (lst)

def main():
    n = int(input("n = "))
    non_Era(n)
    Era(n)

cProfile.run("main()")


# n = 100
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#          62 function calls in 2.555 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 2.py:23(Era)
#         1    0.000    0.000    2.555    2.555 2.py:36(main)
#         1    0.000    0.000    0.000    0.000 2.py:7(non_Era)
#         1    0.000    0.000    2.555    2.555 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
#         1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
#         1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#         1    0.000    0.000    2.555    2.555 {built-in method builtins.exec}
#         1    2.555    2.555    2.555    2.555 {built-in method builtins.input}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
