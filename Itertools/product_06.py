"""
Примеры задач на комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 6. Перебор всех пар элементов из двух списков
Перебор всех пар элементов из двух списков
Даны списки: A = [10, 20] и B = ['x', 'y', 'z'].
Получите все пары (a, b), где a ∈ A, b ∈ B.
"""

from itertools import product
A = [10, 20]
B = ['x', 'y', 'z']
pairs = list(product(A, B))
print(pairs)
