"""
Примеры задач на комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 5.
Генерация PIN‑кодов длиной 4 цифры
Создайте список всех возможных 4‑значных PIN‑кодов
(цифры от 0 до 9).
"""
from itertools import product

digits = '0123456789'
pins = [''.join(p) for p in product(digits, repeat=4)]
print(f"Всего PIN‑кодов: {len(pins)}")  # 10 000
print("Первые 5:", pins[:5])

