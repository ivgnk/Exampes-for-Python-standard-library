"""
Примеры задач на вероятность для
комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 6. Вероятность разных цифр в двузначном числе
УСлучайным образом выбирают двузначное число (от 10 до 99).
Какова вероятность, что цифры в нём разные?
"""
from itertools import product

tens = range(1, 10)    # первая цифра (1–9)
units = range(0, 10)   # вторая цифра (0–9)
numbers = list(product(tens, units))  # 90 чисел
different = [num for num in numbers if num[0] != num[1]]  # 81 число
prob = len(different) / len(numbers)
print(f"P(разные цифры) = {prob:.2f}")  # 0.90