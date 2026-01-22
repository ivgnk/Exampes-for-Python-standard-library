"""
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

2. Перестановки заданной длины
Задача: из букв «ABCD» составить все 2‑буквенные перестановки (порядок важен, повторений букв нет).
"""

from itertools import permutations

letters = "ABCD"
for perm in permutations(letters, 2):
    print(''.join(perm))