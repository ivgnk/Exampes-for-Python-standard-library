"""
Примеры задач на вероятность для
комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 7. Вероятность «орёл-решка» в любом порядке при двух бросках
Монету бросают дважды.
Какова вероятность получить один «орёл» и один «решку» (порядок не важен)?
"""
from itertools import product

tosses = ['О', 'Р']
outcomes = list(product(tosses, repeat=2))  # 4 исхода: ОО, ОР, РО, РР
favorable = [seq for seq in outcomes if seq.count('О') == 1]  # ОР, РО → 2 исхода
prob = len(favorable) / len(outcomes)
print(f"P(О и Р) = {prob:.1f}")  # 0.5

print(f'{len(range(0,10))=}')
print(f'{len(product(tosses, repeat=2))=}')
