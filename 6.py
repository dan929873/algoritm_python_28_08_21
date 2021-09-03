# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это бу

from idna import unichr

x = int(input("char number = "))
print(str(unichr(x+65)))
