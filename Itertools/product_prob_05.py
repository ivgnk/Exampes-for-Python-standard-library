"""
Примеры задач на вероятность для
комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 5. Вероятность хотя бы одной шестёрки при двух бросках кубика
Условие. Бросают кубик дважды. Найдите вероятность,
что хотя бы в одном броске выпадет 6.
"""
from itertools import product

dice = range(1, 7)
outcomes = list(product(dice, repeat=2))  # 36 исходов
favorable = [roll for roll in outcomes if 6 in roll]
# все пары с 6 → 11 исходов (6,1)..(6,6) и (1,6)..(5,6)
print(f'Благоприятные исходы =\n{favorable}')
prob = len(favorable) / len(outcomes)
print(f"P(хотя бы одна 6) = {prob:.3f}")  # 0.306

