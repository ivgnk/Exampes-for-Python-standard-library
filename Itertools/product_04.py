"""
Примеры задач на комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 4.
Моделирование бросков двух шестигранных кубиков
Условие. Симулируйте все возможные исходы при
броске двух 6‑гранных кубиков. Каждый исход — пара чисел (d1, d2).
"""

from itertools import product
dice = range(1, 7)  # 1..6
outcomes = list(product(dice, dice))
print(f"Всего исходов: {len(outcomes)}")
# Вывод в столбик
# for roll in outcomes:
#     print(roll)

# Выводим по 6 кортежей в строке
for i in range(0, len(outcomes), 6):
    row = outcomes[i:i+6]
    print('  '.join(str(tup) for tup in row))



