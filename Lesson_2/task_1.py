# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.

my_super_list = [56, 23.5, 5+6j, "ola!", True, (1, 3, 5), ['wow', 'list in list!'], {8, 'element'}, {'key_1': 888, 'key_2': "aloha!"}, None]

print(my_super_list)

for ind, el in enumerate(my_super_list, 1):
    print(ind, el)
    print(type(el))