# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
# за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.


def fact(n):
    fact_list = []
    res = 1
    for i in range(1, n + 1):
        res *= i
        fact_list.append(res)
    return fact_list


def generator(n):
    for el in fact(n):
        yield el


print(generator(8))
for el in generator(8):
    print(el)
