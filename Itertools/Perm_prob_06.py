"""
Примеры задач на определение вероятности событий с решением
их на Python с использованием permutations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

6. Вероятность, что ни одна буква не осталась на своём месте (перестановка без неподвижных точек)
Условие
Буквы слова «КОД» перемешивают. Какова вероятность, что ни одна буква не останется на исходной позиции?
Логика
Исходное слово: «К», «О», «Д».
Всего перестановок: 3!=6.
Перестановки без неподвижных точек (анаграммы):  «О», «Д», «К»  и  «Д», «К», «О»
Благоприятных: 2.
Вероятность: P=2/6 ≈0,3333.
"""
from itertools import permutations
word = "КОД"
original = list(word)
all_perms = list(permutations(word))
favorable = 0

for perm in all_perms:
    # проверяем, что ни один символ не на своём месте в perm
    lst=[perm[i] != original[i] for i in range(len(original))]
    if all(lst): # Return True if bool(x) is True for all values x
        favorable += 1

probability = favorable / len(all_perms)
print(f"P = {probability:.4f}")  # 0.3333


