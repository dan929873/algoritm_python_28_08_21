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
