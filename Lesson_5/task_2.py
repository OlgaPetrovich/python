# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("new_file.txt", "r", encoding='utf-8') as file_obj:
    lines = 0
    words = 0

    for line in file_obj:
        lines += line.count("\n")
        words = line.split()
        print(f"Количество слов в строке: ", len(words))

    print(f"Количество строк: {lines}")
