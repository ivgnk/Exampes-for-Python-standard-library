"""
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

6. Сохранение перестановок в список
Задача: собрать все перестановки строки «XYZ» в список строк для дальнейшей обработки.
"""

from itertools import permutations

result = list(permutations("XYZ")) # преобразуем в список

print("Все перестановки:", result)
print("Количество:", len(result))

