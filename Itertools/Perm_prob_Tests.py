"""
Создание вариатов заданий для
Примеры задач на определение вероятности событий с решением
их на Python с использованием permutations из itertools
https://alice.yandex.ru/chat/019bdcb5-9025-4000-b4ec-dc4b43a5760d/

"""
lst = ('Рок', 'Рожь', 'Срок', 'Стриж', 'Короб', 'Морось', 'Оркестр',
       'Бригада', 'Бройлер', 'Самокатчик', 'Абракадабра', 'Председатель',)

def count_vowels(word):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

for x in lst:
    print(f'{x:13} длина={len(x):2} гласных={count_vowels(x)}')

