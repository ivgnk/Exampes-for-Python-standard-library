# https://ru.wikipedia.org/wiki/Числа_Фибоначчи
# https://ru.wikipedia.org/wiki/Обобщённые_числа_Фибоначчи
# https://ru.wikipedia.org/wiki/Категория:Числа_Фибоначчи
# https://ru.wikipedia.org/wiki/Категория:Целочисленные_последовательности
#
# https://en.wikipedia.org/wiki/Fibonacci_number
# https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers
# https://en.wikipedia.org/wiki/Category:Fibonacci_numbers
# https://en.wikipedia.org/wiki/Category:Integer_sequences

# A Python Guide to the Fibonacci Sequence
# https://realpython.com/fibonacci-sequence-python/

# Fibonacci numbers from Modules
# https://docs.python.org/3.8/tutorial/modules.html

def fib2(n:int)->list:   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    print(fib2(8000))


