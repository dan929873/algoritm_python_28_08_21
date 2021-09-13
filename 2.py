# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import numbers

my_number = input("Please input number: ")
even = 0
odd = 0
try:
    int(my_number)
    for iter in my_number:
        if int(iter) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"even: {even}\nodd: {odd}")
except ValueError:
    print("not input number")
