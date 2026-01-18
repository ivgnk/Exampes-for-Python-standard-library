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
import random
import statistics
import numpy as np
import matplotlib.pyplot as plt

lst=[1, 2, 3, 4, 5]
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




