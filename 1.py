# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

#функция для подсчета размера обьекта

import sys

# hw1
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def my_memory(x):
    print ("\t", x.__class__, sys.getsizeof(x), x)

my_number = input("Please input digit number: ")

my_sum, product = 0, 1
try:
    for i in my_number:

        my_sum += int(i)
        product *= int(i)

    print(f"+: {my_sum}\n*: {product}")
except ValueError:
    print("you do not input number :(")

my_memory(my_sum)
my_memory(product)
my_memory(my_number)

# result in console
# +: 9
# *: 20
# 	 <class 'int'> 28 9
# 	 <class 'int'> 28 20
# 	 <class 'str'> 51 45
