# 4. Определить, какое число в массиве встречается чаще всего.

mas1 = [8, 3, 6, 4, 2, 5, 6, 7, 8, 9]


max_num2 = 0
num = 0
for i in mas1:
    my_iter = i
    max_num1 = 0
    for j in mas1:
        if my_iter == j:
            max_num1 += 1
    if max_num1 > max_num2:
        num = i
        max_num2 = max_num1
print(num)
