"""
https://alice.yandex.ru/chat/019bc6aa-49e2-4000-bbf4-bd183fe898d1/
пример использования метода cdf() из модуля statistics.NormalDist
для вычисления кумулятивной функции распределения (CDF) нормального распределения.

Метод ndist.cdf() - вычисляет вероятность X
используя кумулятивную функцию распределения, вычисляет вероятность того,
что случайная величина X будет меньше или равна x.
Математически она записывается P(X <= x).
"""

# Импортируем необходимые модули
import matplotlib.pyplot as plt
import numpy as np
from statistics import NormalDist

# Создаем нормальное распределение со средним 0 и стандартным отклонением 1
normal_dist = NormalDist(mu=0, sigma=1)

# Создаем массив значений для оси X
x_values = np.linspace(-4, 4, 1000)

# Вычисляем значения CDF для каждого x
cdf_values = [normal_dist.cdf(x) for x in x_values]

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(x_values, cdf_values, label='CDF Normal Distribution', color='blue')

# Добавляем оформление графика
#  график, показывающий, как изменяется вероятность для стандартного нормального распределения.
#  При x=0 вероятность равна 0.5, что соответствует медиане распределения.
#  При x→∞ вероятность стремится к 1, а
#  при x→-∞ — к 0
plt.title('Кумулятивная функция распределения нормального распределения')
plt.xlabel('Значение (x)')
plt.ylabel('Вероятность')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.tight_layout()

# Показываем график
plt.show()

