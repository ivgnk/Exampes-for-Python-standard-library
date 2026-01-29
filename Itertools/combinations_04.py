"""
Примеры задач на сочетания (без повторений)
с решением их на Python с использованием combinations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d

4. Сочетания для разных типов данных
Задача: для каждого элемента списка
(кортеж, список, строка) найти все 2‑буквенные сочетания.
"""

from itertools import combinations

lst=[(1,2,3),[1,2,3],'123']
for el in lst:
    print('\n', el, type(el))
    print("Все сочетания:")
    res=list(combinations(el,2))
    for c in res:
        print(c)
    print("Количество:", len(res))
