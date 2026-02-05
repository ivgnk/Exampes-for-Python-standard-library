"""
Примeры комбинаций с повторениями и с учётом порядка ()
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d

itertools.product()
"""

# 1. Простое декартово произведение
from itertools import product

A = [1, 2]
B = ['a', 'b']
result = list(product(A, B))
print(result) # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# 2. Размещение с повторениями (через repeat)
result = list(product([0, 1], repeat=3))
print(result)

# 3. Генерация строк
for p in product('AB', repeat=2):
    print(''.join(p))
