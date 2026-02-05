"""
Примеры задач на вероятность для
комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 2. Вероятность угадать двузначный PIN с первой попытки
Условие. PIN‑код состоит из 2 цифр (0–9).
Какова вероятность угадать его за одну попытку?
"""
from itertools import product

digits = '0123456789'
pins = list(product(digits, repeat=2))  # 100 комбинаций
prob = 1 / len(pins)  # 1/100
print(f"P(угадать) = {prob:.3f}")  # 0.010

