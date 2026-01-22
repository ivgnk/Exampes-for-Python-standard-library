"""
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Перестановки (без повторений)
1. Все перестановки строки/списка
Задача: вывести все возможные перестановки букв в слове «ABC
"""

from itertools import permutations

word = "ABC"
perms = permutations(word)
for p in perms:
    print(''.join(p))

# Для подсчёта без генерации: число перестановок равно n!

#-------------- Мой тест
import math
print('-- вторая часть --')
word = "ABCC"
perms = list(permutations(word))
for p in perms:
    print(''.join(p))
n=len(perms)
print(f'{n=}  {math.factorial(len(word))=}')

