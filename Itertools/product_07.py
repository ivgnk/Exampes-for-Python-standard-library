"""
Примеры задач на комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 7. Комбинации вкусов мороженого (с повторами)
В кафе 3 вкуса: 'ваниль', 'шоколад', 'клубника'.
Клиент берёт 2 шарика (можно одинаковые).
Перечислите все возможные комбинации.
"""

from itertools import product

flavors = ['ваниль', 'шоколад', 'клубника']
combos = list(product(flavors, repeat=2))
for combo in combos:
    print(' + '.join(combo))
