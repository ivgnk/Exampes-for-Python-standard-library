"""
Примеры задач на определение вероятности событий с решением
их на Python с использованием permutations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

1. Вероятность конкретного порядка букв в слове
Условие
Слово «КОТ» перемешивают случайным образом. Какова вероятность, что получится именно «КОТ»?
Логика
Всего перестановок 3 букв: 3!=6.
Благоприятный исход — 1 (только «КОТ»).
Вероятность: P=1/6 ≈0,1667.
"""
from itertools import permutations

word = "КОТ"
all_perms = list(permutations(word))
favorable = 1  # только один вариант — "КОТ"
probability = favorable / len(all_perms)
print(f"P = {probability:.4f}")  # 0.1667

