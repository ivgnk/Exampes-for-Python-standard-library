"""
https://docs-python.ru/standart-library/modul-statistics-python/

NormalDist - это инструмент для создания нормальных распределений случайной величины и управления ими.
https://docs-python.ru/standart-library/modul-statistics-python/klass-normaldist-modulja-statistics/
"""

import numpy as np
import statistics
import matplotlib.pyplot as plt

# mu=0.0 - среднее арифметическое данных
# sigma=1.0 - среднее квадратическое отклонение данных
# sigma<0, то возникает ошибка
# Экземпляры statistics.NormalDist() поддерживают
# сложение, вычитание, умножение и деление на константу
ndist = statistics.NormalDist(mu=0.0, sigma=1.0)

# Атрибуты и методы объекта NormalDist.
# Атрибут (только для чтения) ndist.mean - среднее арифметическое нормального распределения,
# Атрибут (только для чтения) ndist.median - медиана нормального распределения,
# Атрибут (только для чтения) ndist.mode - наиболее распространенный элемент данных,
# Атрибут (только для чтения) ndist.stdev - стандартное отклонение нормального распределения,
# Атрибут (только для чтения) ndist.variance - дисперсия нормального распределения,

# Метод ndist.samples() - n случайных выборок для данного среднего и стандартного отклонения
# задаем размер окна
plt.figure(figsize=(12, 8))
n=100
plt.suptitle(f'Распределение случаейных выборок для {ndist}')
for i in range(6):
    dat=ndist.samples(n)
    plt.subplot(2,3,i+1)
    plt.title(f"{len(dat)=}")
    plt.hist(dat, bins=50)
    plt.grid()
    n=n*5
plt.show()



# Метод ndist.pdf() используя функцию плотности вероятности, вычисляет относительную вероятность того,
# что случайная величина X будет близка к заданному значению x.
# Математически это предел отношения P (x <= X < x+dx) / dx, когда dx приближается к нулю.

# https://alice.yandex.ru/chat/019bbb6e-6f37-4000-8748-1f007c54e199/
# Функция pdf() (probability density function) вычисляет значение функции плотности вероятности
# для нормального распределения в заданной точке
# Функция pdf() полезна для:
# - Анализа вероятности появления конкретных значений
# - Построения графиков нормального распределения
# - Сравнения значений в разных точках распределения
# - Проверки соответствия данных нормальному распределению

for x in [-3, -2, -1, 0, 1, 2, 3]:
    pdf_value = ndist.pdf(x)
    print(f"Значение PDF при {x=}  : {pdf_value}")

# Генерируем значения для графика
x_values = np.linspace(-4, 4, 100)
pdf_values = [ndist.pdf(x) for x in x_values]
# Строим график
plt.plot(x_values, pdf_values)
plt.title(f'Функция плотности нормального распределения\n{ndist}')
plt.xlabel('Значение (x)'); plt.ylabel('Плотность вероятности')
plt.grid(); plt.show()

# несколько графиков с разными sigma
plt.title(f'Функции плотности нормального распределения\nпри разных сигма')
for sgm in [1.0, 0.3, 3.0]:
    ndist = statistics.NormalDist(mu=0.0, sigma=sgm)
    pdf_values = [ndist.pdf(x) for x in x_values]
    plt.plot(x_values, pdf_values, label=f'sigma={sgm}')
plt.legend()
plt.grid(); plt.show()

# Метод ndist.inv_cdf() - вычисляет обратную кумулятивную функцию распределения,
# Метод ndist.overlap() - измеряет соответствие между двумя нормальными распределениями вероятностей,
# Метод ndist.quantiles() - делит нормальное распределение на n непрерывных интервалов,
# Метод ndist.zscore() - вычисляет стандартную оценку.
