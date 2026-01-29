"""
Примеры задач на сочетания (без повторений)
с решением их на Python с использованием combinations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d

Сочетания элементов списка (не строк)
Задача: получить все 2‑элементные сочетания из списка [10, 20, 30, 40]
"""

from itertools import combinations

data = [10, 20, 30, 40]
for combo in combinations(data, 2):
    print(combo)

data = ['10', '20', '30', '40']
for combo in combinations(data, 2):
    print(combo)
