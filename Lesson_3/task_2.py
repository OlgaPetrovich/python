# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info(**kwargs):
    return kwargs


user_name = input("Введите ваше имя: ")
user_surname = input("Введите вашу фамилию: ")
user_birth_year = input("Введите год вашего рождения: ")
user_city = input("Введите город вашего проживания: ")
user_email = input("Введите ваш email: ")
user_phone_num = input("Введите ваш телефон: ")

print(user_info(name=user_name, surname=user_surname, birth_year=user_birth_year, city=user_city, email=user_email, telephone=user_phone_num))
