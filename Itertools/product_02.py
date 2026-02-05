"""
Примеры задач на комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 2.
Перебор комбинаций параметров
Условие. Есть три параметра:

color ∈ ['red', 'blue'];
size ∈ ['S', 'M', 'L'];
material ∈ ['cotton', 'polyester'].

Выведите все возможные комбинации параметров.
"""
from itertools import product
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
materials = ['cotton', 'polyester']

for combo in product(colors, sizes, materials):
    print(combo)



