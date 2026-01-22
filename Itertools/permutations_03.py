"""
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

3. Подсчёт числа перестановок
Задача: сколько существует перестановок букв в слове «МАТЕМАТИКА» (учесть повторяющиеся буквы)?
"""

from itertools import permutations

word = "МАТЕМАТИКА"
# Генерируем все перестановки и считаем уникальные
unique_perms = set(permutations(word))
print(f"Число уникальных перестановок: {len(unique_perms)}")


