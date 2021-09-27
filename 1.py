# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib

set_hash = set()
my_str = input('Enter a string containing only small Latin letters: ')

for i in range(len(my_str)):
    for j in range(len(my_str), i, -1):
        hash_str = hashlib.sha1(my_str[i:j].encode('utf-8')).hexdigest()
        set_hash.add(hash_str)

print(f'{len(set_hash) + 1} different substrings in a string - {my_str}')
