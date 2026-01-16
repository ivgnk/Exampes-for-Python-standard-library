"""
https://alice.yandex.ru/chat/019bc6aa-49e2-4000-bbf4-bd183fe898d1/

метод zscore() объекта NormalDistй позволяет вычислить z-оценку (стандартизированное значение)
для заданного значения.
Z-оценка показывает, на сколько стандартных отклонений значение отклоняется от среднего.
"""

from statistics import NormalDist


print('-----------------------1-----------------------')
# Создаем нормальное распределение
dist = NormalDist(mu=70, sigma=10)  # среднее 70, стандартное отклонение 10

# Значения для расчета z-оценки
values = [50, 60, 70, 80, 90]

# Рассчитываем z-оценки
z_scores = [dist.zscore(value) for value in values]

# Выводим результаты
for value, z in zip(values, z_scores):
    print(f"Значение: {value}, Z-оценка: {z:.2f}")

# Пример с другим распределением
height_dist = NormalDist(mu=175, sigma=7)  # распределение роста
person_height = 185
z = height_dist.zscore(person_height)
print(f"\nРост человека: {person_height} см, Z-оценка: {z:.2f}")

# Значение: 50, Z-оценка: -2.00
# Значение: 60, Z-оценка: -1.00
# Значение: 70, Z-оценка: 0.00
# Значение: 80, Z-оценка: 1.00
# Значение: 90, Z-оценка: 2.00
#
# Рост человека: 185 см, Z-оценка: 1.43

# Важные характеристики метода:
# Возвращает число с плавающей точкой
# Положительное значение означает, что значение больше среднего
# Отрицательное значение — значение меньше среднего
# 0 означает, что значение равно среднему
#
# Практическое применение:
# - Оценка относительного положения значения в распределении
# - Сравнение значений из разных распределений
# - Выявление выбросов
# - Стандартизация данных


print('-----------------------2-----------------------')
print('первый график')
import matplotlib.pyplot as plt
import numpy as np

# Создаем данные для графика
x = np.linspace(dist.mean - 4*dist.stdev, dist.mean + 4*dist.stdev, 1000)
z_values = [dist.zscore(val) for val in x]

plt.figure(figsize=(10, 6))
plt.plot(x, z_values, label='Z-оценка', color='blue')
plt.scatter(values, z_scores, color='red', zorder=5)

plt.title('График Z-оценок')
plt.xlabel('Исходное значение')
plt.ylabel('Z-оценка')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(dist.mean, color='gray', linestyle='--', label='Среднее значение')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print('-----------------------3-----------------------')
print('второй график')
# Создаем распределение
dist = NormalDist(mu=70, sigma=10)  # mu = 70, sigma = 10

# Получаем доступ к параметрам
mean = dist.mean    # среднее значение
stdev = dist.stdev  # стандартное отклонение (то же самое, что dist.sigma)

# Создаем данные для графика
x = np.linspace(
    dist.mean - 4*dist.stdev,  # от среднего минус 4 сигмы
    dist.mean + 4*dist.stdev,  # до среднего плюс 4 сигмы
    1000
)

z_values = [dist.zscore(val) for val in x]

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(x, z_values, label='Z-оценка', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(dist.mean, color='gray', linestyle='--', label='Среднее значение')
plt.title('График Z-оценок')
plt.xlabel('Исходное значение')
plt.ylabel('Z-оценка')
plt.grid(True)
plt.legend()
plt.show()
