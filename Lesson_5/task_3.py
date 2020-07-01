# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
# окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("text_3.txt", 'r', encoding='utf-8') as file_obj:
    sum_good = []
    bad_salary = []
    line = file_obj.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            bad_salary.append(i[0])
        sum_good.append(i[1])

aver_sal = sum(map(float, sum_good)) / len(sum_good)

print(f"Зарплату меньше 20 000 получают: {bad_salary},")
print(f"Средняя зарплата (среди работников, получающих больше 20 000): {aver_sal}")
