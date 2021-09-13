# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


def my_calculation(x1, x2, s):
    if s == '-':
        return x1 - x2
    if s == '+':
        return x1 + x2
    if s == '*':
        return x1 * x2
    if s == '/':
        return x1 / x2


s = 'n'
simbol_ligal = [ '+', '-', '*', '/']
while(s != '0'):
    try:
        x1 = float(input("number 1 = "))
        s = input("simbol = ")
        x2 = float(input("number 2 = "))
        if s in simbol_ligal:
            if s == '/' and x2 == '0':
                print("not correct to divide by zero")
                continue
            print(f"result: {my_calculation(x1, x2, s)}")
        elif s != '0':
            print("you not correct simbol, for exit '0'")
            continue
    except ValueError:
        print("Please input number")
        continue
else:
    print("Bye my user")
