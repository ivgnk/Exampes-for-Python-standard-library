"""
Примеры задач на сочетания (без повторений)
с решением их на Python с использованием combinations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d

1. Все сочетания из N по K
Задача: из букв «ABCDE» выбрать все возможные 3‑буквенные сочетания
(порядок не важен).
"""
import sys
from itertools import combinations
#--- без повтора
def fun1():
    letters = "ABCDE"
    print('\n строка = '+letters)
    from itertools import combinations
    res=list(combinations(letters, 3))
    for i, combo in enumerate(res):
        print(i,''.join(combo))

    #--- с повтором
    letters = "ABABE"
    print('\n строка = '+letters)
    res=list(combinations(letters, 3))
    for i, combo in enumerate(res):
        print(i,''.join(combo))

# fun1()
# sys.exit()

from itertools import combinations
letters = ["ABCDE","ABABE"]
res = [list(combinations(let, 3)) for let in letters ]
llen=max([len(r) for r in res])
for i in range(llen):
    print(i,end=' ')
    print(''.join(res[0][i]), end=' ')
    print(''.join(res[1][i]))

