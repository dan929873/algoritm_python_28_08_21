# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

#функция для подсчета размера обьекта

import sys

def show_sizeof(x, level=0):
    print ("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)

# hw1
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

my_number = input("Please input digit number: ")

my_sum, product = 0, 1
try:
    for i in my_number:

        my_sum += int(i)
        product *= int(i)

    print(f"+: {my_sum}\n*: {product}")
except ValueError:
    print("you do not input number :(")

show_sizeof(my_sum)
show_sizeof(product)
show_sizeof(my_number)

# Please input digit number: 21
# +: 3
# *: 2
#  <class 'int'> 28 3
#  <class 'int'> 28 2
#  <class 'str'> 51 21
