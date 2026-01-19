"""
Программа на Python для выделения точки с выбросом и ее устранения при условии
модуль разности среднего значения и текущего больше 3 стандартных отклонений
https://alice.yandex.ru/chat/019bd59b-7912-4000-a9c4-8dfef52a8af8/
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Создаем тестовый набор данных
data = [5, 2, 4.5, 4, 3, 2, 6, 20, 9, 2.5, 3.5, 4.75, 6.5, 2.5, 8, 1]
a=0
data =[102+a, 98+a, 99+a, 100+a, 97+a, 140+a, 95+a, 100+a, 98+a, 96+a, 102+a, 101+a, 101+a, 102+a, 99+a, 102+a]

df = pd.DataFrame(data, columns=['Значение'])

# Вычисляем среднее и стандартное отклонение
mean = df['Значение'].mean()
std = df['Значение'].std()

# Определяем порог для выбросов
threshold = 3

# Находим выбросы
outliers = df[(abs(df['Значение'] - mean) > threshold * std)]

# Удаляем выбросы
cleaned_data = df[(abs(df['Значение'] - mean) <= threshold * std)]

# Визуализация результатов
plt.figure(figsize=(12, 6))

# Исходные данные
plt.subplot(1, 2, 1)
plt.scatter(df.index, df['Значение'], color='blue', label='Исходные данные')
plt.scatter(outliers.index, outliers['Значение'], color='red', label='Выбросы')
plt.title('Исходные данные с выбросами'); plt.grid()
plt.legend()

# Очищенные данные
plt.subplot(1, 2, 2)
plt.scatter(cleaned_data.index, cleaned_data['Значение'], color='green', label='Очищенные данные')
plt.title('Данные после удаления выбросов')
plt.legend()

plt.tight_layout()
plt.show()

print("Исходные данные:\n", df)
print("\nВыявленные выбросы:\n", outliers)
print("\nОчищенные данные:\n", cleaned_data)

