"""
Примеры задач на определение вероятности событий с решением
их на Python с использованием permutations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

5. Вероятность, что порядок букв соответствует алфавиту
Условие
Буквы «Б», «А», «Р» перемешивают. Какова вероятность, что они выстроятся в алфавитном порядке («А», «Б», «Р»)?
Логика
Всего перестановок: 3! = 6.
Благоприятный исход: 1.
Вероятность: P = 1/6 ≈ 0,1667.
"""
from itertools import permutations

letters = ["Б", "А", "Р"]
sorted_order = tuple(sorted(letters))  # ("А", "Б", "Р")
all_perms = list(permutations(letters))
if sorted_order in all_perms:
    favorable = 1
else:
    favorable =0

probability = favorable / len(all_perms)
print(f"P = {probability:.4f}")  # 0.1667

