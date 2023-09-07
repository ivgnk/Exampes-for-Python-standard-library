import math
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
''' 
модуль math в Python
1) Функции округления чисел
https://docs-python.ru/standart-library/modul-math-python/funktsii-okruglenija-chisel-modulja-math/
Функция math.trunc() отбрасывает дробную часть числа x. Результат будет целым числом.
Функция math.floor() возвращает x округленное в меньшую сторону до ближайшего целого.
Функция math.ceil() возвращает x округленное в большую сторону до ближайшего целого.

2) Степенные и логарифмические функции модуля math
https://docs-python.ru/standart-library/modul-math-python/stepennye-logarifmicheskie-funktsii/
Функция math.pow() возвращает x в степени y.
Функция math.sqrt() возвращает квадратный корень числа x.
Функция math.cbrt() возвращает кубический корень из числа x.
Функция math.log(x[, base]) возвращает логарифм числа x по основанию base. 
Если аргумент base не указан, то возвращается натуральный логарифм числа x.
Функция math.log(x, base) эквивалентна выражению log(x)/log(base)
Функция math.log10() возвращает десятичный логарифм числа x, 
вычисление которого происходит немного точнее, чем math.log(x, 10)
Функция math.log2() возвращает двоичный логарифм числа x, 
вычисление которого происходит немного точнее, чем math.log(x, 2).
Функция math.log1p() возвращает натуральный логарифм от x + 1 , 
значение которого расчитывается более точно, особенно для небольших чисел.
Функция math.exp() возвращает e, возведенное в степень x, 
где e=2.718281… - основание натуральных логарифмов. 
Функция считает более точно, чем math.e ** x или math.pow(math.e, x)
Функция math.exp2() возвращает 2, возведенное в степень x.
Функция math.expm1() возвращает e**x - 1, 
которое вычисляется значительно точнее, чем math.exp(x) - 1, 
особенно для небольших чисел x.

3) тригонометрические функции модуля math
https://docs-python.ru/standart-library/modul-math-python/trigonometricheskie-funktsii-modulja-math/
Функция math.sin();
Функция math.cos();
Функция math.tan();
Функция math.asin();
Функция math.acos();
Функция math.atan();
Функция math.atan2();
Функция math.hypot() возвращает евклидову норму, sqrt(sum(x**2 for x in coordinates)). 
Это длина вектора от начала координат до точки, заданной координатами.
Для двумерной точки (x, y) это эквивалентно вычислению гипотенузы 
прямоугольного треугольника с использованием теоремы Пифагора sqrt(x*x + y*y).
Изменено в Python 3.8: Добавлена поддержка n-мерных точек. 
Раньше поддерживался только двумерный случай.

4) Функции преобразование меры углов модуля math в Python
https://docs-python.ru/standart-library/modul-math-python/funktsii-preobrazovanie-mery-uglov-modulja-math/
Функция math.degrees() преобразует угол x из радиан в градусы.
Функция math.radians() преобразует угол x из градусов в радианы.

5) Гиперболические функции модуля math
https://docs-python.ru/standart-library/modul-math-python/giperbolicheskie-funktsii-modulja-math/
Функция math.sinh(),
Функция math.cosh(),
Функция math.tanh(),
Функция math.asinh(),
Функция math.acosh(),
Функция math.atanh().

6) Константы и специальные значения модуля math
https://docs-python.ru/standart-library/modul-math-python/konstanty-spetsialnye-znachenija-modulja-math/
Константа Рi,
Константа e,
Константа Inf,
Константа NaN,
Функция math.isinf() возвращает True в случаях, 
когда x является отрицательной или положительной бесконечностью, 
иначе возвращает False.
Функция math.isnan() возвращает True если x является nan, иначе возвращает False.
Функция math.isfinite() возвращает False если x является либо nan, 
либо inf или -inf, во всех остальных случаях возвращается True.

7) Специальные функции модуля math
https://docs-python.ru/standart-library/modul-math-python/spetsialnye-funktsii-modulja-math/
Функция math.erf() возвращает значение функции ошибок от указанного значения аргумента x.
Функция math.erfc() возвращает значение дополнительной функции ошибок от указанного значения аргумента x. 
Эквивалентна команде 1 - erf(x).
Функция math.gamma() возвращает значение гамма функции от указанного аргумента x.
Функция math.lgamma() возвращает значение натурального логарифма от модуля гамма функции при заданном значении 
аргумента x. Данная функция эквивалентна выражению math.log(abs(math.gamma(x))).
'''

def thetest_special_functions():
    x = np.linspace(-3, 3, 60)
    y_erf = np.linspace(-3, 3, 60)
    y_erfc = np.linspace(-3, 3, 60)
    x_gam = np.linspace(0.1, 3, 60)
    y_gam = deepcopy(x_gam)
    y_lgam = deepcopy(x_gam)
    llen = x.size
    for i in range(llen):
        y_erf[i] = math.erf(x[i])
        y_erfc[i] = math.erfc(x[i])
        y_gam[i] = math.gamma(x_gam[i])
        y_lgam[i] = math.lgamma(x_gam[i])
    plt.plot(x,y_erf, label = 'erf')
    plt.plot(x,y_erfc, label = 'erfc')
    plt.plot(x_gam,y_gam, label = 'gamma')
    plt.plot(x_gam,y_lgam, label = 'lgamma')
    plt.grid()
    plt.legend()
    plt.show()



if __name__ == "__main__":
    thetest_special_functions()