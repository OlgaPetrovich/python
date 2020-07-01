# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
my_list = []
while True:
    new_str = input("Введите строку (для окончания ввода нажмите 'Enter'): ")
    if new_str == '':
        print(my_list)
        exit()
    else:
        user_str = new_str + '\n'
        my_list.append(user_str)

    with open("new_file.txt", "w", encoding='utf-8') as file_obj:
        file_obj.writelines(my_list)
