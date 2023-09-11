'''
2022 Как изменилась стандартная библиотека Python за последние годы
https://habr.com/ru/articles/665020/
docs.python.org/3.9/library/bisect.html

https://pythonworld.ru/moduli/modul-bisect.html
Модуль bisect работает с отсортированными списками методом бинарного поиска. Основные функции:
bisect() находит элемент в списке;
insort() добавляет элемент, сохраняя порядок.
'''

import bisect

lst = [7, 11, 19, 42]
print(lst)
# bisect.bisect(list, elem, lo=0, hi=len(a)), или bisect.bisect_right(list, elem, lo=0, hi=len(a)) —
# поиск места для вставки элемента в отсортированный список,
# таким образом, чтобы elem располагался как можно правее.
idx = bisect.bisect(lst,12)
print(idx)
# Вставьте x в отсортированном порядке . Это эквивалентно предположению, что a уже отсортировано.
# Имейте в виду, что при поиске O(log n) преобладает медленный шаг вставки
bisect.insort(lst,12)
print(lst)

