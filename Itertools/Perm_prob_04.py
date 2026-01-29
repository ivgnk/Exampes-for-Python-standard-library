"""
Примеры задач на определение вероятности событий с решением
их на Python с использованием permutations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

4. Вероятность, что перестановка начинается и заканчивается на одну букву
Условие
Буквы слова «РАДАР» перемешивают. Какова вероятность, что слово начинается и заканчивается на «Р»?
Логика
Всего уникальных перестановок: 4!/2!  =12 (две «А»).
Фиксируем «Р» на первом и последнем месте. Остаются: «А», «Д», «А»
Перестановок оставшихся: 3!/2! =3
Вероятность: P=3/12 =0,25
"""
from itertools import permutations

word = "РАДАР"
all_perms = set(permutations(word))
favorable = 0

for perm in all_perms:
    if perm[0] == perm[-1] == "Р":
        favorable += 1

probability = favorable / len(all_perms)
print(f"P = {probability:.4f}")  # 0.2500


