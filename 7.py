# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


my_number = int(input("Please input number: "))
res1 = 0
res2 = my_number*(my_number+1)/2
for iter in range(my_number+1):
    res1 += iter

print(f"{res1 == res2}")
