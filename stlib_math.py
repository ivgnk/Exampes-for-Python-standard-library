import math
# Функции относящиеся к теории чисел
# https://docs-python.ru/standart-library/modul-math-python/funktsii-teorii-chisel-modulja-math/

def thetest_gcd():
# возвращает наибольший общий делитель указанных целочисленных аргументов *integers.
# в Python 3.9 добавлена поддержка произвольного количества аргументов
    print(f'наибольший общий делитель {math.gcd(3886, 9048)=}')
    print(f'наибольший общий делитель {math.gcd(16, 24)=}')
    print(f'наибольший общий делитель {math.gcd(16, 24, 15)=}')
    print(f'наибольший общий делитель {math.gcd(16, 24, 150)=}')

def reverse_frexp(m, e)->float:
    return m*(2**e)
def thetest_frexp():
    # Функция math.frexp() возвращает кортеж из двух чисел (m, e) таких что x == m*2**e.
    (m,e) = math.frexp(150)
    print(f'мантисса и показател степени 2 {math.frexp(150)=}  {reverse_frexp(m, e)=}')


if __name__ == "__main__":
    # thetest_gcd()
    # print(math.ulp(0.1))
    thetest_frexp()