"""
https://alice.yandex.ru/chat/019bc6aa-49e2-4000-bbf4-bd183fe898d1/
"""

from statistics import NormalDist

# Python модуль statistics, объект statistics.NormalDist, значения по умолчанию для объекта
print('\n----------------------1----------------------')
print('объект statistics.NormalDist, значения по умолчанию для объекта')

# Создание стандартного нормального распределения
std_normal = NormalDist()

print(f"Среднее: {std_normal.mean}")    # 0.0
print(f"Стандартное отклонение: {std_normal.stdev}")  # 1.0
print(f"Медиана: {std_normal.median}")  # 0.0
print(f"Мода: {std_normal.mode}")       # 0.0

# Важно отметить, что при попытке создать объект с отрицательным значением sigma
# будет вызвано исключение StatisticsError, так как стандартное отклонение не может быть отрицательным.


# Python модуль statistics, объект statistics.NormalDist, задать все значения не по умолчанию
print('\n----------------------2----------------------')
print('объект statistics.NormalDist, задать все значения не по умолчанию')
# Создаем нормальное распределение с заданными параметрами
custom_dist = NormalDist(
    mu=50,          # среднее значение
    sigma=10        # стандартное отклонение
)

# Альтернативный способ создания через метод from_samples
data = [45, 55, 48, 52, 49, 51, 53, 47, 50, 54]
sample_dist = NormalDist.from_samples(data)

# Вывод параметров распределения
print("Параметры пользовательского распределения:")
print(f"Среднее (mu): {custom_dist.mean}")        # 50
print(f"Стандартное отклонение (sigma): {custom_dist.stdev}")  # 10
print(f"Медиана: {custom_dist.median}")          # 50
print(f"Мода: {custom_dist.mode}")               # 50

print("\nПараметры распределения по выборке:")
print(f"Среднее: {sample_dist.mean}")
print(f"Стандартное отклонение: {sample_dist.stdev}")

# Важные моменты при настройке:
#
# 1/ Параметры mu и sigma можно задавать любыми числами, но:
# = sigma должно быть положительным (больше 0)
# = mu может быть любым действительным числом
#
# 2/ Методы создания:
# = Прямое задание параметров (mu и sigma)
# = Создание из выборки данных через from_samples()
#
# 3/ Доступ к параметрам:
# mean — среднее значение
# stdev — стандартное отклонение
# median — медиана
# mode — мода
#
# 4/ Ограничения:
# = Нельзя создать распределение с sigma ≤ 0
# =При использовании from_samples() требуется как минимум две различные точки данных

# Дополнительные возможности
print('\n----------------------3----------------------')
print('Дополнительные возможности')
# Модификация существующего распределения
modified_dist = custom_dist * 2  # умножение на константу

# Сложение распределений
another_dist = NormalDist(mu=20, sigma=5)
combined_dist = custom_dist + another_dist

print("\nМодифицированное распределение:")
print(f"Новое среднее: {modified_dist.mean}")  # 100
print(f"Новое стандартное отклонение: {modified_dist.stdev}")  # 20

print("\nКомбинированное распределение:")
print(f"Среднее: {combined_dist.mean}")  # 70
print(f"Стандартное отклонение: {combined_dist.stdev}")  # ~11.18

# При работе с распределениями важно помнить, что:
# Среднее значение определяет центр распределения
# Стандартное отклонение определяет разброс значений
# Все статистические характеристики автоматически пересчитываются при изменении параметров

# Последний пример с "Дополнительные возможности" сделай с графиками в Matplotlib
print('\n----------------------4----------------------')
print('Дополнительные возможности c графиками')

import matplotlib.pyplot as plt
import numpy as np
from statistics import NormalDist

# Создаем исходные распределения
custom_dist = NormalDist(mu=50, sigma=10)
another_dist = NormalDist(mu=20, sigma=5)

# Модифицируем распределения
modified_dist = custom_dist * 2
combined_dist = custom_dist + another_dist

# Функция для построения PDF
def plot_normal_dist(dist, color, label):
    x = np.linspace(dist.mean - 4*dist.stdev, dist.mean + 4*dist.stdev, 1000)
    pdf = [dist.pdf(val) for val in x]
    plt.plot(x, pdf, color=color, label=label, linewidth=2)

# Создаем график
plt.figure(figsize=(14, 8))
# Исходное распределение
plot_normal_dist(custom_dist, 'blue', 'Исходное (mu=50, sigma=10)')
# Второе распределение
plot_normal_dist(another_dist, 'orange', 'Второе (mu=20, sigma=5)')
# Модифицированное умножением
plot_normal_dist(modified_dist, 'green', 'Модифицированное (умножение на 2)')
# Комбинированное
plot_normal_dist(combined_dist, 'red', 'Комбинированное (сложение)')

# Оформление графика
plt.title('Сравнение нормальных распределений', fontsize=16)
plt.xlabel('Значение', fontsize=14)
plt.ylabel('Плотность вероятности', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.tight_layout()

# Добавляем текстовые аннотации
plt.text(50, custom_dist.pdf(50), f'μ={custom_dist.mean:.1f}\nσ={custom_dist.stdev:.1f}',
         color='blue', ha='center', va='bottom')

plt.text(20, another_dist.pdf(20), f'μ={another_dist.mean:.1f}\nσ={another_dist.stdev:.1f}',
         color='orange', ha='center', va='bottom')

plt.text(100, modified_dist.pdf(100), f'μ={modified_dist.mean:.1f}\nσ={modified_dist.stdev:.1f}',
         color='green', ha='center', va='bottom')

plt.text(70, combined_dist.pdf(70), f'μ={combined_dist.mean:.1f}\nσ={combined_dist.stdev:.1f}',
         color='red', ha='center', va='bottom')

plt.show()

#  что показывает этот график:
# Исходное распределение (синим цветом):
# Среднее = 50
# Стандартное отклонение = 10
#
# Второе распределение (оранжевым):
# Среднее = 20
# Стандартное отклонение = 5
# Модифицированное распределение (зеленым):
# Получено умножением исходного на 2
# Среднее = 100
# Стандартное отклонение = 20
#
# Комбинированное распределение (красным):
# Результат сложения двух распределений
# Среднее = 70
# Стандартное отклонение ≈ 11.18
# На графике видно:
# - Как меняется форма кривой при изменении параметров
# - Как влияет умножение на константу
# - Как происходит сложение распределений
# - Как меняются центры и разбросы
