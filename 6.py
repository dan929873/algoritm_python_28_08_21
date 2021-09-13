# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. 
# Если за 10 попыток число не отгадано, то вывести загаданное число.



from random import random
n = round(random() * 100)
i = 1
print("Computer thought of a number. Guess it. You have 10 attempts")
while i <= 10:
    u = int(input(str(i) + 'attempt: '))
    if u > n:
        print('many')
    elif u < n:
        print('little')
    else:
        print(f'You guessed it right on {i} dth try')
        break
    i += 1
else:
    print(f'You have exhausted 10 attempts. It was envisioned{n}')
