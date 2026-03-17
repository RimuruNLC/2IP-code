import pandas as pd
import random as rd
# 1 метод создание массива со своими индексами
data = pd.Series([rd.randint(0,10) for _ in range(30)])
print(data)
# 2 метод достаем значение с помощью индекса
print(data[3])
# 3 метод узнаем количество предметов внутри
print(len(data), data.size)
# 4 метод узнаем уникальные предметы внутри
print(data.unique())
# 5 метод узнаем кол-во значений
print(data.value_counts())
# 6 метод узнаем тип данных
print(data.dtypes)
# 7 метод создания дата фрейма
dict1 = {
    "Города":["Шумерля","Чебоксары"],
    "Темпаратура":["5","4"],
    "Численность населения":["26 873+","497 061+"]
}
data1 = pd.DataFrame(dict1)
print(data1)
# 8 метод Отображает указанное кол-во строк
print(data1.head(1))
# 9 метод Дает информацию об датафрейме
print("----------------")
print(data1.info())
# 10 метод Срезы 
print(data1[:])
