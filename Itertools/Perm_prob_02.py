"""
Примеры задач на определение вероятности событий с решением
их на Python с использованием permutations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

2. Вероятность, что гласная стоит на первом месте
Условие
Буквы слова «АИСТ» перемешивают. Какова вероятность, что первая буква — гласная?
Логика
Гласные: «А», «И» (2 буквы).
Всего перестановок: 4!=24.
Для каждой гласной на первом месте: 3!=6 перестановок оставшихся букв.
Благоприятных исходов: 2×6=12.
Вероятность: P=12/24 =0,5.
"""
from itertools import permutations

word = "АИСТ"
vowels = {"А", "И"}
all_perms = list(permutations(word))
favorable = 0 # переменная для подсчета благоприятных исходов
for perm in all_perms:
    if perm[0] in vowels:
        favorable += 1
probability = favorable / len(all_perms)
print(f"P = {probability:.4f}")  # 0.5000
