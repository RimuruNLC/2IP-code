import pandas as pd
pd.set_option('display.max_columns', None)
tablica = pd.read_excel("bebebebe.xlsx")
print("Топ по Компьютерные сети")
print(tablica[["Ф.И. Студента","Компьютерные сети"]].sort_values("Компьютерные сети",ascending=False))
print("Топ по Основы алгоритмизации и программирования")
print(tablica[["Ф.И. Студента","Основы алгоритмизации и программирования"]].sort_values("Основы алгоритмизации и программирования",ascending=False))
print("Топ по Разработка программых модулей")
print(tablica[["Ф.И. Студента","Разработка программых модулей"]].sort_values("Разработка программых модулей",ascending=False))
print("Топ по Системное программирование")
print(tablica[["Ф.И. Студента","Системное программирование"]].sort_values("Системное программирование",ascending=False))
list1 = []
time_propusk = list(tablica["Пропущено часов занятий: Всего"])
for i in time_propusk:
    list2 = i.split(" ")
    print(i)
    list1.append(int(int(list2[0])/2))
tablica["Количество двоек за пропуски"] = list1
tablica["Средний балл"] = tablica[["Компьютерные сети","Основы алгоритмизации и программирования","Разработка программых модулей","Системное программирование"]].mean(axis=1)
print(tablica)
