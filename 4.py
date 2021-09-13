# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

my_n = int(input("Please input number: ")) - 1
ferst = 1
result = 1
for iter in range(my_n):
    result += ferst / 2
    ferst = ferst / 2

print(result)
