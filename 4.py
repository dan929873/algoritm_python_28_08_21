# 4. Написать программу, которая генерирует в указанных пользователем границах:
#
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.

import random

x = int(input("\tinteger 1 = "))
y = int(input("\tinteger 2 = "))
print(random.randint(x, y))

x = float(input("\tfloat 1 = "))
y = float(input("\tfloat 2 = "))
print(random.uniform(x, y))

x = input("\tchar 1 = ")
y = input("\tchar 2 = ")
print(chr(random.randrange(ord(x), ord(y))))
