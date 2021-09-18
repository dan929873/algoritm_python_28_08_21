# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.


numbers_firm = int(input("numbers firm: "))
number_report = 4
firm = [["" for j in range(number_report+2)] for i in range(numbers_firm)]
mean = 0
for i in range(numbers_firm):
    firm[i][0] = input("name firm: ")
    firm[i][number_report + 1] = 0
    for j in range(number_report):
        firm[i][j+1] = int(input(f"{firm[i][0]}, {j+1} quarterly profit: "))
        firm[i][number_report+1] += firm[i][j+1]
    firm[i][number_report+1] = firm[i][number_report+1] / number_report
    mean += firm[i][number_report+1]
mean = mean/numbers_firm

for k in range(numbers_firm):
    if firm[k][number_report + 1] > mean:
        print(f"{firm[k][0]}  >  mean ")
    elif firm[k][number_report + 1] < mean: 
        print(f"       mean  >  {firm[k][0]}")

