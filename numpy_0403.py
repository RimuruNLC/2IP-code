import random
import numpy as np
import math
def start():
    while True:
        str_polz = str(input("Введите строку состоящую минимум из 4 слов \n>"))
        list1 = str_polz.split(' ')
        if len(list1) >3:
            break
        else:
            print("В вашем предложении меньше 4 слов!")
    return list1
def formatirovanie(list1):
    list_final = []
    str_alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    list_alf = list(str_alf)
    for i in list1:
        str1 = ""
        x = 0
        if i.isalpha():
            list_final.append(str(len(i)))
        elif i.isdigit() and int(i) > 0 and int(i) <6:
            str1 = ""
            for j in range(int(i)):
                str1 += str_alf[random.randint(0,len(str_alf)-1)]
            list_final.append(str1)
    return list_final
def numpy_matrix(list1):
    # x = 1
    # while True:
    #     if x**2 >= len(list1):
    #         break
    #     else:
    #         x+=1
    x = math.ceil(math.sqrt(len(list1)))
    while (x*x)!=len(list1):
        list1.append("0")
    matrix = np.array(list1)
    matrix.resize(x,x)
    return matrix
print(numpy_matrix(formatirovanie(start())))
