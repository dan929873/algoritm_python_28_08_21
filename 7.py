# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним

x = input("length 1 = ")
y = input("length 2 = ")
z = input("length 3 = ")

if x > 0 and y > 0 and z > 0:
    print("this triangle may exist")
    if x != y and x != z and y != z:
        print("versatile triangle")
    if x == y or x == z or y == z:
        print("isosceles triangle")
    if x == y and x == z and y == z:
        print("equilateral triangle")
        
