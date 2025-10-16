# -*- coding: utf8 -*-
# str1 = "final 78"
# a = 78
# b = "78"
# if str1.isalpha():
#     print("True")
# elif str1.isdigit():
#     print("123")
# elif str1.isupper():
#     print("verhniy registr")
#
# str4 = "Hello, sergey"
#
# if str4.startswith("Hello"):
#     print("Hello")
#
# str7 = "ssssssss"
# print(str7.upper())
# str8 = "HOHOHOHOHOHO"
# print(str8.lower())
#
# name_user = input("vvedite vashe imya = ")
# print(name_user.strip())
#
# str_kaki = "Hello sergey and timofey"
# print(str_kaki.find("and"))
#
# str_new = str_kaki.replace("sergey", "gaggaga")
# print(str_new)
# del str_kaki
#
# str_hahaha = "Hello world"
# str_hahaha_new = str_hahaha.split(" ")
# print(str_hahaha_new)
# str1= "hello, world"
# list1 = list(str1)
#
# str2 = "".join(list1)
# print(str2)

# Получить от пользователя предложение из пяти слов
# В двух словах имеются числа
# Полученную строку преобразовать в список слов
# Слова, там где есть числа преобразовать в заглавные буквы
# А в тех словах где чисел нет, преобразовать
# только первые символы в заглавные
# После преобразования, собрать полученые слова в строку

str1 = input("Введите предложение из пяти слов (в двух из них должны быть числа) - ")
list1 = str1.split(" ")
for i in list1:
    if i.isalpha() == 0:
        list1.insert(list1.index(i), i.upper())
        list1.remove(i)
    else:
        list1.insert(list1.index(i), i.title())
        list1.remove(i)
str_final = " ".join(list1)
print(str_final)