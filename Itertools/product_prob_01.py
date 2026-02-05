"""
Примеры задач на вероятность для
комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 1. Вероятность выпадения суммы 7 при броске двух кубиков
Условие. Бросают два стандартных 6‑гранных кубика.
Найдите вероятность, что сумма очков равна 7.
"""
from itertools import product

dice = range(1, 7)
outcomes = list(product(dice, dice))
favorable = [roll for roll in outcomes if sum(roll) == 7]
print(f'{len(outcomes)=}')
print(f'{favorable=}')
prob = len(favorable) / len(outcomes)
print(f"P(сумма=7) = {prob:.3f}")  # 0.167

