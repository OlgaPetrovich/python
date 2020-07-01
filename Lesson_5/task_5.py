# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("new_text_5.txt", 'w', encoding='utf-8') as f_obj:
    num_sum = 0
    for i in range(10):
        num = randint(1, 100)
        num_sum += num
        f_obj.write(str(num) + " ")

print(f"Сумма всех элементов равна {num_sum}")
