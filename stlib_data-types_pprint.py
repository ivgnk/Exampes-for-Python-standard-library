'''
pprint — Data pretty printer¶
https://docs.python.org/3/library/pprint.html
Красивый вывод списков, словарей и других структур данных
https://docs-python.ru/standart-library/modul-pprint-python/
'''
import pprint

def pp_1():
    '''
    Класс PrettyPrinter() модуля pprint в Python
    https://docs-python.ru/standart-library/modul-pprint-python/klass-prettyprinter-modulja-pprint/
    '''
    print('\npart 0 - список с форматированием по умолчанию')
    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    pp = pprint.PrettyPrinter()
    pp.pprint(stuff)
    # ['spam', 'eggs', 'lumberjack', 'knights', 'ni']

    print('\npart 1 - список')
    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    pp = pprint.PrettyPrinter(indent=4, width=40)
    pp.pprint(stuff)
    # [   'spam',
    #     'eggs',
    #     'lumberjack',
    #     'knights',
    #     'ni']

    print('\npart 2 - список списков')
    stuff.insert(0, stuff[:])
    pp.pprint(stuff)
    # [   [   'spam',
    #         'eggs',
    #         'lumberjack',
    #         'knights',
    #         'ni'],
    #     'spam',
    #     'eggs',
    #     'lumberjack',
    #     'knights',
    #     'ni']

    print('\npart 3 - компактный список списков')
    pp = pprint.PrettyPrinter(width=40, compact=True)
    pp.pprint(stuff)
    # [['spam', 'eggs', 'lumberjack',
    #   'knights', 'ni'],
    #  'spam', 'eggs', 'lumberjack',
    #  'knights', 'ni']

    print('\npart 4 - форматирование с многоточием')
    tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', ..., ('parrot', ('fresh fruit',))))))))
    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(tup)
    # ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))

def pp_2():
    '''
    Методы объекта PrettyPrinter модуля pprint в Python
    https://docs-python.ru/standart-library/modul-pprint-python/metody-obekta-prettyprinter-modulja-pprint/
    '''

    print('\npart 1')
    # Метод PrettyPrinter.pformat() возвращает отформатированное представление объекта object в виде 'строки',
    # при этом учитываются параметры, передаваемые конструктору pprint.PrettyPrinter.
    stuff_d = {'one': 'spam', 'two': 'eggs', 'three':'lumberjack', 'four': 'knights', 'five': 'ni'}
    pp = pprint.PrettyPrinter(width=40)
    ss = pp.pformat(stuff_d)
    print(ss)

    print('\npart 2')
    # Метод PrettyPrinter.pprint() распечатает отформатированное представление объекта object
    # в настроенном потоке с последующим переводом строки.
    pp.pprint(stuff_d)

    print('\npart 3')
    # Метод PrettyPrinter.isreadable() определяет, является ли отформатированное представление объекта object
    # "читабельным" или может использоваться для восстановления значения с помощью функции eval().
    # метод возвращает False для рекурсивных объектов.
    # Если в PrettyPrinter задан параметр глубины depth и переданный объект object глубже, чем разрешено, то возвращается False.
    print(f'{pp.isreadable(stuff_d) = }')

    print('\npart 4 ')
    # Метод PrettyPrinter.isrecursive() определяет, требует ли объект рекурсивного представления. Э
    # тот метод используется в качестве ловушки, чтобы подклассы могли изменять способ преобразования объектов в строки.
    print(f'{pp.isrecursive(stuff_d) = }')


def pp_3():
    '''
    Печать отформатированных структур данных
    https://docs-python.ru/standart-library/modul-pprint-python/funktsija-pp-modulja-pprint/
    '''
    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    pprint.pp(stuff, width=41)

def pp_4():
    '''
    Функция pprint() модуля pprint в Python
    https://docs-python.ru/standart-library/modul-pprint-python/funktsija-pprint-modulja-pprint/
    '''

    # Функция pprint() модуля pprint печатает отформатированное представление объекта
    # в потоке stream с последующим переводом строки.
    # Если аргумент stream=None, используется sys.stdout.
    # Это поведение можно использовать в интерактивном интерпретаторе вместо функции print() для проверки значений.
    stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    pprint.pprint(stuff, width=40)
    print()
    stuff_d = {'one':'spam', 'two':'eggs', 'three':'lumberjack', 'four':'knights', 'five':'ni'}
    pprint.pprint(stuff_d, width=40)

if __name__ == "__main__":
    pp_4()

