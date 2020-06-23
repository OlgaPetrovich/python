# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(a_1, a_2, a_3):

    if a_1 < a_2 and a_1 < a_3:
        max_sum = a_2 + a_3
    elif a_2 < a_1 and a_2 < a_3:
        max_sum = a_1 + a_3
    else:
        max_sum = a_1 + a_2
    return print(f"Сумма наибольших двух аргументов равна {max_sum}")


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))

my_func(num_1, num_2, num_3)
