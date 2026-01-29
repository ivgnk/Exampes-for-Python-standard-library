"""
Примеры задач на сочетания (без повторений)
с решением их на Python с использованием combinations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d

5. Сочетания без повторяющихся букв (в исходной строке есть дубли)
Задача: из строки «AABC» выбрать все уникальные 2‑буквенные сочетания
"""


from itertools import combinations
word = "AABC"
res=list(combinations(word,2))
print('Исходное сочетание',res)
# Используем set(), чтобы убрать дубли сочетаний из‑за повторяющихся 'A'
unique_combos = set(res)
print('уникальные 2‑буквенные сочетания')
for combo in unique_combos:
    print(''.join(combo))

