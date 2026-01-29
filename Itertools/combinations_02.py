"""
Примеры задач на сочетания (без повторений)
с решением их на Python с использованием combinations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d

2. Подсчёт числа сочетаний
Задача: сколько существует 4‑элементных сочетаний из 10 элементов?
"""

from itertools import combinations
n = 10
k = 4
count = len(list(combinations(range(n), k)))
print(f"C({n}, {k}) = {count}")


