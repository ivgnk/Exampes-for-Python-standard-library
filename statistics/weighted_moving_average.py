"""
# Среднее взвешенное
# https://alice.yandex.ru/chat/019bbbae-a1e7-4000-9aa2-99bd75f6c7e4/


"""
import numpy as np
import matplotlib.pyplot as plt

print('\nСреднее взвешенное')
def weighted_moving_average(data, window_size, weights=None):
    """
    Вычисление взвешенного скользящего среднего
    :param data: исходные данные
    :param window_size: размер окна фильтрации
    :param weights: веса для каждого элемента окна
    :return: отфильтрованные данные
    """
    if weights is None:
        # Равномерные веса по умолчанию
        weights = np.ones(window_size)

    # Нормализация весов
    weights = np.array(weights) / np.sum(weights)

    result = np.convolve(data, weights, mode='valid')

    # Дополнение начала массива для сохранения длины
    padding = np.zeros(window_size - 1)
    print(f'{len(data)=}')     #100
    print(f'{len(weights)=}')  # 7
    print(f'{len(result)=}')   # 94
    print(f'{len(padding)=}')  # 6
    res=np.concatenate([padding, result]) # объединения нескольких массивов в один вдоль указанной оси
    print(f'{res=}')   # в res - первые 6 нули из padding, далее - result
    return res


# Пример использования
if __name__ == "__main__":
    # Генерация тестовых данных
    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.2, 100)

    # Параметры фильтрации
    window = 7
    weights = np.array([1, 2, 3, 4, 3, 2, 1])  # Пример весов

    # Применение фильтра
    filtered = weighted_moving_average(y, window, weights)

    # Визуализация результатов
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label='Исходные данные', alpha=0.5)
    plt.plot(x, filtered, label='Взвешенное скользящее среднее', color='red')
    plt.legend()
    plt.title('Фильтр взвешенного скользящего среднего')
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.grid(True)
    plt.show()
