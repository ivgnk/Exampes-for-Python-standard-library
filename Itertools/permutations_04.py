"""
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

4. Перестановки с фильтрацией по условию
Задача: из цифр [1, 2, 3, 4] составить все 3‑значные числа,
где первая цифра не равна 1.
"""

from itertools import permutations

digits = [1, 2, 3, 4]
res=permutations(digits, 3)
print(type(res)) # результат permutations - <class 'itertools.permutations'>
res=list(res) # преобразуем в список
print(type(res[0])) # элементы списка имеют <class 'tuple'>
print(type(res[0][0])) # элементы кортежа(tuple) имеют <class 'int'>

valid_numbers = []
for perm in res:
    if perm[0] != 1:  # первая цифра не 1
        valid_numbers.append(perm)

print(f"Найдено {len(valid_numbers)} вариантов:")
for num in valid_numbers:
    s = ''.join(map(str, num)) # объединяем элементы кортежа в строку
    print(s)
print(type(s)) # <class 'str'>
