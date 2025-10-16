# import os
# import time
#
# import sys
# print(os.getcwd())
# a = os.getcwd()
# print(type(a))
# print(os.listdir())
# b = os.listdir()
# print(b[2])
# # os.mkdir("бебебебубубу")
# time.sleep(0.5)
# print(os.listdir())
# # os.remove("")
# # os.rmdir("бебебебубубу")
#
# print(os.listdir())
# # os.rename("проекты", "projects")
# l1 = os.path.exists('projects')
# print(l1)
# os.rename("07.10.py", 'D:\python2IP')
import os
import sys

# print(os.getcwd()) # Получает путь
# a = os.getcwd()
# print(type(a))
# print(os.listdir()) # Выводит объекты в виде списка
# b = os.listdir()
# print(type(b))
# print(b[2])
#
# # os.mkdir("test") # Создает папку
# # os.mkdir("test2")
# # os.mkdir("test3")
# # os.rmdir("test3")
# print(os.listdir())
# # os.rename('test.txt','test2.txt')
# print(os.listdir())
# l1 = os.path.exists('test2.txt') # поревряет существование файла
# print(l1)
# # os.remove('test2.txt')
# print(os.path.exists('test2.txt'))
# os.rename('test2.txt','D:/PythonProject10/test2/test2.txt')
# os.mkdir("New papka")
import time
print(os.getcwd())
time.sleep(1)
print(os.listdir())
time.sleep(1)
os.rename('D:/python2IP/вот_это_переноси.txt', 'D:/python2IP/New papka/вот_это_переноси.txt')
print(os.listdir())
time.sleep(1)
os.rename('D:/python2IP/New papka/вот_это_переноси.txt', 'D:/python2IP/вот_это_переноси.txt')
print(os.listdir())
print("я хочу домой ")