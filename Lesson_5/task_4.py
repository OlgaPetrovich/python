# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "''": "''"}

with open("new_text_4.txt", 'a', encoding='utf-8') as file_obj:
    with open("text_4.txt", 'r', encoding='utf-8') as f_obj:
        line = f_obj.read().split('\n')
        try:
            for i in line:
                i = i.split(" - ")
                file_obj.writelines(rus[i[0]] + " - " + i[1] + "\n")
        except KeyError:
            print(" ")
