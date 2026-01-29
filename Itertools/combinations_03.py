"""
Примеры задач на сочетания (без повторений)
с решением их на Python с использованием combinations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d

3. Сочетания с фильтрацией по условию
Задача: из чисел [1, 2, 3, 4, 5] выбрать все 3‑элементные сочетания,
где сумма элементов > 7.
"""

from itertools import combinations

numbers = [1, 2, 3, 4, 5]
valid_combos = []
res=list(combinations(numbers, 3))
print(f'Всего combinations {len(res)}')

for i,combo in enumerate(res):
    s= sum(combo); usl= s > 7

    if usl:
        valid_combos.append(combo)
    print(f'{i}  {combo}  {s:2}   s > 7 == {usl}')

print(f"Найдено {len(valid_combos)} вариантов для условия")



