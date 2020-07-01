# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

result = []
with open("new_text_7.json", 'w', encoding='utf-8') as file_obj:
    with open("text_7.txt",'r', encoding='utf-8') as f_obj:
        prof = {}
        for line in f_obj:
            prof[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        aver_prof = sum([int(i) for i in prof.values() if int(i) > 0]) / len([int(i) for i in prof.values() if int(i) > 0])
        result.append(prof,)
        result.append({"Average_sum": round(aver_prof)})
    json.dump (result, file_obj)