"""
Операции с множествами в Python, подсчёт числа элементов
"""

# Объединение
print('\nОбъединение')
a = [1, 2, 3]
b = [3, 4, 5]
ab = set(a + b)
print(f'{ab=} {len(ab)=}')

a = {1, 2, 3}
b = {3, 4, 5}
un1 = a | b
un2 = a.union(b)
print(f'{un1=} {len(un1)=}')
print(f'{un2=} {len(un2)=}')

# Пересечение
print('\nПересечение')
a = {1, 2, 3}
b = {3, 4, 5}
res = a & b
print(f'{res=} {len(res)=}')

# Разность
print('\nРазность')
a = {1, 2, 3};  b = {3, 4, 5}
res1 = a - b;  res2 = b - a
print(f'{res1=} {len(res1)=}')
print(f'{res2=} {len(res2)=}')

# Дополнение
print('\nДополнение')
U = {1, 2, 3, 4, 5}  # универсальное множество
A = {1, 2}
res = U - A
print(f'{res=} {len(res)=}')

# Декартово произведение
print('\nДекартово произведение ')
A = {1, 2}
B = {'x', 'y'}
res = {(a, b) for a in A for b in B}
print(f'{res=}   {len(res)=}')  # {(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')}

res=set()
for a in A:
    for b in B:
        pair = (a, b)      # формируем пару
        res.add(pair)    # добавляем пару во множество
print(f'{res=}   {len(res)=}')  # {(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')}

from itertools import product
A = {1, 2}
B = {'x', 'y'}
res = set(product(A, B))
print(f'{res=}   {len(res)=}')  # {(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')}
