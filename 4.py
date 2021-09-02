# 4. Написать программу, которая генерирует в указанных пользователем границах:
#
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.

import random
import string

x = float(input("\tx1 = "))
y = float(input("\ty1 = "))

print(random.randint(x, y))
print(random.uniform(x, y))
print(''.join(random.choice(string.ascii_letters)))
