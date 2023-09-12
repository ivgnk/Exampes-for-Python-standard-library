'''
2022 Как изменилась стандартная библиотека Python за последние годы

Модуль itertools предоставляет разнообразные итераторы для эффективной работы
с коллекциями (эффективной с точки зрения использования памяти).
https://habr.com/ru/articles/665020/

https://docs.python.org/3/library/itertools.html

2020 Itertools в Python https://habr.com/ru/companies/otus/articles/529356/

Введение в модуль itertools Python https://docs-python.ru/standart-library/modul-itertools-python/vvedenie-modul-itertools/
Модуль itertools в Python, эффективные итераторы для циклов https://docs-python.ru/standart-library/modul-itertools-python/
'''
import inspect
import itertools

# Бесконечные итераторы.
# При их использовании необходимо понимать,
# что в конце концов нужно будет как то выходить из этих итераторов,
# иначе будет бесконечный цикл


def thetest_count():
    '''
    itertools.count() будет возвращать равномерно распределенные значения,
    начиная с числа, которое передается в качестве начального параметра start;
    этот итератор также принимает параметр шага step.
    '''
    print('\nФункция = ', inspect.currentframe().f_code.co_name)
    for i in itertools.count(10):
        if i > 15:
            break
        else:
            print(i)

def thetest_count_with_slice():
    '''
    itertools.islice() выполняет срез бесконечного итератора
    (обычная операция среза последовательности не работает с типом итератор)
    itertools.islice(iterable, stop)
    itertools.islice(iterable, start, stop[, step])
    iterable - итератор,
    start - int, начало среза,
    stop - int, конец среза (не входит),
    step - int, шаг среза.
    https://docs-python.ru/standart-library/modul-itertools-python/funktsija-islice-modulja-itertools/
    islice()не поддерживает отрицательные значения для start , stop или Step .
    https://docs.python.org/3/library/itertools.html#itertools.islice
    '''
    for i in itertools.islice(itertools.count(10), 25):
        print(i)

if __name__ == "__main__":
    thetest_count_with_slice()