"""
Примеры задач на определение вероятности событий с решением
их на Python с использованием permutations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

3. Вероятность, что две заданные буквы стоят рядом
Условие
Буквы слова «МАМА» перемешивают. Какова вероятность, что две «М» окажутся рядом?
Логика
Всего перестановок с учётом повторов: 4!/(2!⋅2!) =6
«М» рядом: считаем «ММ» как один блок
Тогда перестановки: («ММ», «А», «А») дают 3!/2! = 3
Вероятность: P=3/6=0,5
"""
from itertools import permutations

word = "МАМА"
all_perms = set(permutations(word))  # уникальные перестановки
favorable = 0
for perm in all_perms:
    # проверяем, есть ли подряд две «М»
    for i in range(len(perm) - 1):
        if perm[i] == perm[i + 1] == "М":
            favorable += 1
            break

probability = favorable / len(all_perms)
print(f"P = {probability:.4f}")  # 0.5000
