"""
Примеры задач на комбинации с повторениями и с учётом порядка,
используя функцию product из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

Задача 3.
Поиск всех трёхбуквенных слов из заданного алфавита
Условие. Используя буквы 'A', 'B', 'C',
сгенерируйте все трёхбуквенные «слова»
(буквы могут повторяться).
"""

from itertools import product
alphabet = 'ABC'
for word in product(alphabet, repeat=3):
    print(''.join(word))


