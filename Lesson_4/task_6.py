# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count,cycle
from sys import argv

script_name, first_num, user_str = argv

for el in count(int(first_num)):
    if el > 10:
        break
    else:
        print(el)

i = 0
for el in cycle(user_str):
    if i > 10:
        break
    print(el)
    i += 1