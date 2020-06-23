# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через lis4t и через dict.

month_num = int(input("Введите месяц в виде целого числа от 1 до 12: "))
dict_seasons = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
list_seasons = ["зима", "весна", "лето", "осень"]

if month_num == 12 or month_num == 1 or month_num == 2:
    print(f"Введенный вами месяц относится к сезону {dict_seasons.get(1)}")
    print(f"Введенный вами месяц относится к сезону {list_seasons[0]}")
elif month_num == 3 or month_num == 4 or month_num == 5:
    print(f"Введенный вами месяц относится к сезону {dict_seasons.get(2)}")
    print(f"Введенный вами месяц относится к сезону {list_seasons[1]}")
elif month_num == 6 or month_num == 7 or month_num == 8:
    print(f"Введенный вами месяц относится к сезону {dict_seasons.get(3)}")
    print(f"Введенный вами месяц относится к сезону {list_seasons[2]}")
elif month_num == 9 or month_num == 10 or month_num == 11:
    print(f"Введенный вами месяц относится к сезону {dict_seasons.get(4)}")
    print(f"Введенный вами месяц относится к сезону {list_seasons[3]}")
else:
    print("Вы ввели несуществующий месяц.")
