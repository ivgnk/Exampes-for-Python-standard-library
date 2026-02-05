"""
Примеры задач на вероятность для
комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 3. Вероятность двух орлов при трёх бросках монеты
Условие. Монету бросают 3 раза.
Найдите вероятность ровно двух «орлов» (О) и одного «решки» (Р).
"""
from itertools import product

tosses = ['О', 'Р']
sequences = list(product(tosses, repeat=3))  # 8 исходов
favorable = [seq for seq in sequences if seq.count('О') == 2]  # ООР, ОРО, РОО → 3 исхода
prob = len(favorable) / len(sequences)
print(f"P(2 орла) = {prob:.3f}")  # 0.375

