# tuple1 = 1,2,3,4,5
# for i in tuple1:
#     print(i)
# tuple2 = (1,2,3,4,5)
# print(tuple2)
# list1 = list(tuple2)
# list1.append(1342342)
# tuple2= tuple(list1)
# print(tuple2)

# slovai

# dicr1= {
#     "1":23,
#     23:23,
#     'wewre':'werg',
#     (2,3):True,
# }
# print(dicr1)
# print(dicr1["1"])
# print(dicr1[(2,3)])
# dict3 = {
#     1:1,
#     2:2,
#     3:3,
#     4:4,
#     5:5
# }
# print(dict3)

# x = 0
# while x < 2:
#       student = {
#         "name":"Timofey",
#         "familiya":"Danilov",
#         "rassa":"Human",
#         "dr":"15.12.2008",
#         "Stipuha":721,
#         "Planeta":"Earth",
#         "strana":"Russia",
#         "adress":"Shumerlya",
#         "pred":["Informatica","Istoria"],
#         "youarehuman?":"no",
#         "youareguest?":"yes"
#       }
#       x+=1
#       # print(student[input("что хочешь узнать? - ")])
#       # if x == 2:
#       #     print("\nя устал..")
# print(student["Stipuha"])
# student["Stipuha"] = 1220
# print(student["Stipuha"])
# student1 = student.copy()
# print(student1)
# student1.update({123: 123})
# a = student1.pop("dr")
# print(student1)
# print(a)
# print(student1.keys())
# student1.setdefault("dr")
# print(student1)


#
# student = {
#         "name":"Timofey",
#         "familiya":"Danilov",
#         "rassa":"Human",
#         "dr":"15.12.2008",
#         "Stipuha":721,
#         "Planeta":"Earth",
#         "strana":"Russia",
#         "adress":"Shumerlya",
#         "pred":["Informatica","Istoria"],
#         "youarehuman?":"no",
#         "youareguest?":"yes"
#       }

import time
print("библиотека номеров:\n 111  123  432\n 964  990  001\n 002  235  701")
time.sleep(1)
input("кому ты хочешь позвонить ? - ")
x=0
while x<=5:
    telef = {
        "111":"здравствуйте?",
        "123":"оу.. ПРИВЕТ ДРУГ!",
        "432":"ХВАТИТ МНЕ ЗВОНИТЬ!!",
        "964":"Ало?",
        "990":"Ой..куда я жмал..",
        "001":" ",
        "002":" ",

    }