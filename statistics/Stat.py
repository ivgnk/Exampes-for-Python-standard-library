"""
https://docs.python.org/3/library/statistics.html
https://docs-python.ru/standart-library/modul-statistics-python/
https://sky.pro/wiki/analytics/modul-statistics-v-python-obrabotka-dannyh-s-primerami-koda/
https://digitology.tech/docs/python_3/library/statistics.html
https://chelcenter.susu.ru/chel-center.ru/python-yfc/2020/02/11/opisatelnaya-statistika-na-python-chast-1/index.html

https://www.geeksforgeeks.org/python/statistics-with-python/
https://dzen.ru/a/aO9LrQwzC3tT_hVt
"""

import math
import statistics
from cProfile import label

import numpy as np
import random
import matplotlib.pyplot as plt

lst=[1, 2, 3, 4, 5]
print(f'{math.fsum(lst)=}')
print(f'{statistics.mean(lst)=}')

print('--------------------------')
print('среднее для обыкновенной дроби')
from fractions import Fraction as F
print(f'{statistics.mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])=}') # Fraction(13, 21)
print(f'{statistics.fmean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])=}') # 0.6190476190476191
print(f'{float(F(13, 21))=}')  # 0.6190476190476191
print('--------------------------')
print(f'{statistics.fmean(lst)=}')
print(f'{statistics.geometric_mean(lst)=}')

# Вычисляем среднее квадратическое значение
rms = math.sqrt(statistics.mean(x**2 for x in lst))
print(f'среднее квадратическое значение {rms=}')
# Вычисляем среднее кубическое значение
cubes = statistics.mean([x**3 for x in lst])
mean_cubes = cubes**(1/3)
print(f'среднее кубическое значение {mean_cubes=}')


# Ручное вычисление среднего геометрического
prd=math.prod(lst); print(f'{prd=}')
g_m=math.pow(prd, 1/len(lst)); print(f'{g_m=}')
print(f'{statistics.harmonic_mean(lst)=}')
print(f'{statistics.median(lst)=}')
print(f'{statistics.median([1, 3, 5, 7])=}')
print(f'{statistics.median_low([1, 3, 5, 7])=}')
print(f'{statistics.median_high([1, 3, 5, 7])=}')

# Функция mode() модуля statistics возвращает единственный
# наиболее распространенный элемент данных data из дискретных или номинальных данных.
# Если в последовательности существует несколько значений с одинаковой частотой
# распространения, то эта функция возвращает первый из них.
print(f'{statistics.mode(lst)=}')
print(f'{statistics.mode([1, 2, 2, 3, 3, 5])=}')
print(f'{statistics.mode(["red", "blue", "blue", "red", "green", "red", "red"])=}')
# Наиболее часто встречающиеся элементы в последовательности
print(f'{statistics.multimode(lst)=}')
print('стандартное отклонение генеральной совокупности')
print(f'{statistics.pstdev(lst)=}');psd=statistics.pstdev(lst)
print('дисперсия генеральной совокупности')
print(f'{statistics.pvariance(lst)=} проверка {psd*psd=}')
print('стандартное отклонение выборки')
print(f'{statistics.stdev(lst)=}')
print('дисперсия выборки'); sd=statistics.stdev(lst)
print(f'{statistics.variance(lst)=} проверка {sd*sd=}')
print()
print('-----------Проверка для массивов numpy')
npa=np.array(lst)
print(f'{type(npa)=}')
print(f'{math.fsum(npa)=}')
print(f'{statistics.mean(npa)=}')
print(f'{statistics.fmean(npa)=}')
print(f'{statistics.geometric_mean(npa)=}')
print(f'{statistics.harmonic_mean(npa)=}')
print('стандартное отклонение генеральной совокупности')
print(f'{np.std(npa)=}')
print('стандартное отклонение выборки')
print(f'{np.std(npa,ddof=1)=}')

print('-----------среднее для набора данных')
x = np.arange(-10.0, 10.1, 0.2)
y = - x + x**2- 0.1*x**3 # + x**2 - 0.1*x**3
rnd = np.array([random.uniform(0,1) for i in range(len(x))])
k=[0.8, 0.4, 0.2]
ynew= np.empty(len(k), dtype=object)
for i,d in enumerate(k):
    noise1 = d*y*rnd
    dat=y + noise1
    print(f'{i=} {len(dat)=}')
    ynew[i]=dat

plt.title('Кривые с шумом')
plt.plot(x, y, label='ini')
print(f'{len(ynew)=}')
print(f'{len(ynew[0])=}')
for i, d in enumerate(ynew):
    print(f'{i} {len(x)=} {len(d)=}')
    plt.plot(x, d, label=f'ini+rnd*{k[i]}', ls='--')


ynew2=[]
for i,d in enumerate(ynew):
    res=ynew[i]-1.001*min(ynew[i])
    ynew2.append(res)

for i, d in enumerate(ynew2):
    plt.plot(x, d, label=f'Mod -> ini+rnd*{k[i]}', ls='--')

plt.grid(); plt.legend()
plt.show()

sr=statistics.fmean(ynew2[1])
gm=statistics.geometric_mean(ynew2[1])
hm=statistics.harmonic_mean(ynew2[1])
rms = math.sqrt(statistics.mean(x**2 for x in ynew2[1]))
cms =  (statistics.mean(x**3 for x in ynew2[1]))**(1/3)

plt.plot(x, ynew2[1], label=f'dat', ls='-')
plt.axhline(y=sr, color='r',label='средняя')
plt.axhline(y=gm, color='g',label='geometric_mean')
plt.axhline(y=gm, color='k',label='harmonic_mean', ls='--')
plt.axhline(y=rms, color='m',label='среднее квадратическое', ls='--')
plt.axhline(y=cms, color='y',label='среднее кубическое', ls='--')
plt.grid(); plt.legend()
plt.show()




