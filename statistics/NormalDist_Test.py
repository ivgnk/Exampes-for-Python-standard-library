import statistics
from statistics import NormalDist
import numpy as np
import matplotlib.pyplot as plt


def nd_from_sample(sample:list, col: str, lbl:str):
    sd=NormalDist.from_samples(sample)
    print('--------------------')
    print(f'{sample=}')
    print(f"Среднее: {sd.mean}")  # 0.0
    ststdev=sd.stdev
    print(f"Стандартное отклонение: {ststdev}")  # 1.0
    # print(f"Медиана: {sd.median}")  # 0.0
    # print(f"Мода: {sd.mode}")  # 0.0
    if ststdev> 1E-8:
        x = np.linspace(sd.mean - 4*sd.stdev, sd.mean + 4*sd.stdev, 1000)
        pdf = [sd.pdf(val) for val in x]
        plt.plot(x, pdf, color=col, label=lbl, linewidth=2)

    return (sd)
data = [1, 1, 1, 1, 1, 1, 1, 1, 1, ]
sample_dist = nd_from_sample(data, 'blue', str(data))
print(f'{statistics.mean(data)=}')
print(f'{statistics.stdev(data)=}')

data2 = [0, 1, 1, 1, 1, 1, 1, 1, 0 ]
sample_dist = nd_from_sample(data2, 'cyan', str(data2))
print(f'{statistics.mean(data2)=}')
print(f'{statistics.stdev(data2)=}')

data3 = [0, 0, 1, 1, 1, 1, 1, 0, 0 ]
sample_dist = nd_from_sample(data3,'magenta', str(data3))
print(f'{statistics.mean(data3)=}')
print(f'{statistics.stdev(data3)=}')

data4 = [0, 0, 0, 1, 1, 1, 0, 0, 0 ]
sample_dist = nd_from_sample(data4, 'green', str(data4))
print(f'{statistics.mean(data4)=}')
print(f'{statistics.stdev(data4)=}')

plt.title('Сравнение нормальных распределений', fontsize=16)
plt.xlabel('Значение', fontsize=14)
plt.ylabel('Плотность вероятности', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
