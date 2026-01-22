"""
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

3. Подсчёт числа перестановок
Задача: сколько существует перестановок букв в слове «МАТЕМАТИКА» (учесть повторяющиеся буквы)?

используем формулу n!/(n1!*n2!*...nk!),
где n — длина слова, ni — количество повторений каждой буквы,
! -  факториал
"""


import math
word = "МАТЕМАТИКА"
#  подсчет числа появлений каждой буквы в слове
char_count = {} # создаем пустой словарь
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f'{char_count=}')

n=len(word) # длина слова
nn = math.factorial(n)

# Находим n1!*n2!*...nk!, где ni — количество повторений каждой буквы
product = 1
for value in char_count.values(): # цикл по числам в словаре
    product = product*math.factorial(value)
print(f'{product=}')
unique_perms = nn/product
print(f"Число уникальных перестановок:", unique_perms)


