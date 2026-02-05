"""
Примеры задач на комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 1. Генерация всех двузначных двоичных кодов
Условие. Сгенерируйте все возможные
двузначные последовательности из символов 0 и 1.
"""
from itertools import product

for code in product('01', repeat=2):
    print(''.join(code))


