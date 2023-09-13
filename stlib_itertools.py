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
    print('\n1 Count')
    for i in itertools.count(2.5,-5.5):
        if i < -26:
            break
        else:
            print(i)

    print('\n2 Count')
    # https://habr.com/ru/companies/otus/articles/529356/
    l1 = [5, 15, 25]
    l2 = zip(itertools.count(), l1)
    print(list(l2))
    print(list(l2))

    print('\n3 Count')
    l3 = zip(itertools.count(), l1)
    for i in l2:
        print(i)
    print(list(l3))

    print('\n4 Count')
    l1 = map(lambda x: x ** 2, itertools.count())
    for i in l1:
        if i > 50:
            break
        else:
            print(i, end=" ")

def thetest_isslice():
    '''
    islice - Получить срез итератора/генератора
    itertools.islice(iterable, stop)
    itertools.islice(iterable, start, stop[, step])
    iterable - итератор,
    start - int, начало среза,
    stop - int, конец среза (не входит),
    step - int, шаг среза.
    https://docs-python.ru/standart-library/modul-itertools-python/funktsija-islice-modulja-itertools/
    '''
    print(list(itertools.islice('ABCDEFG', 2)))
    # ['A', 'B']
    print(list(itertools.islice('ABCDEFG', 2, 4)))
    # ['C', 'D']
    print(list(itertools.islice('ABCDEFG', 2, None)))
    # ['C', 'D', 'E', 'F', 'G']
    print(list(itertools.islice('ABCDEFG', 0, None, 2)))
    # ['A', 'C', 'E', 'G']

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
    for i in itertools.islice(itertools.count(10), 15):
        print(i)

if __name__ == "__main__":
    # thetest_count()
    # thetest_count_with_slice()
    thetest_isslice()