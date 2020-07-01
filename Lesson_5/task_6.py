# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

new_dict = {}
with open("text_6.txt", 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        subj, amount = line.split(":")
        subj_sum = sum(map(int, "".join([i for i in amount if i == ' ' or ('0' <= i <= '9')]).split()))
        new_dict[subj] = subj_sum
print(f"{new_dict}")
