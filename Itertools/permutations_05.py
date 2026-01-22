"""
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

5. Перестановки элементов списка (не строк)
Задача: переставить элементы списка [10, 20, 30] всеми возможными способами.
"""

from itertools import permutations

data = [10, 20, 30]
for perm in permutations(data):
    print(perm)