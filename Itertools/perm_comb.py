"""
Различие сочетаний и перестановок
"""
print('\n---------- перестановки')
from itertools import permutations
# Все перестановки из 3 элементов
print(list(permutations('ABC')))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'),
#  ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# Перестановки длины 2
print(list(permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

##################################################################
print('\n---------- сочетания')
from itertools import combinations
# Все сочетания длины 2
print(list(combinations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Порядок не создаёт новых сочетаний
print(list(combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]

print('\n---------- перестановки в слове с повторением букв')
print(list(permutations('AAB', 2)))

print('\n---------- сочетания в слове с повторением букв')
print(list(combinations('AAB', 2)))

print('\n----------')
result = list(set(combinations([1, 1, 2], 2)))
print(result)