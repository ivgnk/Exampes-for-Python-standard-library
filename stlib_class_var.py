'''
Поиск = "язык программирования python переменная классов"

2023 Обращение к переменной класса Python
https://uchet-jkh.ru/i/obrashhenie-k-peremennoi-klassa-python
'''
num = 0
class Sudoku(object):
    def __init__(self, data):
        global num
        num = num +1
        self.dat_ = data
        print(num)

class Sudoku2(object):
    num1 = 0
    def __init__(self, data):
        Sudoku2.num1 += 1
        self.dat_ = data
        print(Sudoku2.num1)

dd = Sudoku2(1)
dd2 = Sudoku2(1)