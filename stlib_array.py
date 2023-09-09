'''
docs.python.org/3.9/library/array.html

Модуль array предоставляет компактные однотипные числовые массивы.
Элементы массива в модуле array могут быть следующих типов:
‘i’	- int
‘f’	- float

Подробно https://fullstacker.ru/modul-array-v-python-osnovy-raboty-s-massivami
Кратко https://pythonworld.ru/moduli/modul-array-massivy-v-python.html
Кратко https://pythonz.net/references/named/array/
'''

import array

# Пример из https://pythoninfo.ru/osnovy/massivy-python
example_array = array.array('i', [1, 2, 6, 3, 4]) # первый аргумент указывает на тип элементов. i означает integer
example_array.insert(0, -1)
print('После вставки:', example_array)
example_array.append(-1)
print('После добавления в конец:', example_array)
example_array.extend([5, 6])
print('После объединения со списком:', example_array)
print('Удалён элемент:', example_array.pop(4))
print('После удаления элемента:', example_array)
print('Срез:', example_array[0:4])
# Вывод
# После вставки: array('i', [-1, 1, 2, 6, 3, 4])
# После добавления в конец: array('i', [-1, 1, 2, 6, 3, 4, -1])
# После объединения со списком: array('i', [-1, 1, 2, 6, 3, 4, -1, 5, 6])
# Удалён элемент: 3
# После удаления элемента: array('i', [-1, 1, 2, 6, 4, -1, 5, 6])
# Срез: array('i', [-1, 1, 2, 6])

