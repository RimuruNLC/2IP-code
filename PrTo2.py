import pandas as pd
def to10_2(a):
    str_final=""
    while a > 0:
        str_final += str(a%2)
        a//=2
    str_final = str_final[::-1]
    while len(str_final)!=6:
        str_final = "0"+str_final
    return str_final
alf_russ = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
alf = pd.Series([to10_2(i+1) for i in range(len(alf_russ))], index=alf_russ)
print(alf)
list1 = []
for i in str(input("Введите предложение из русских букв\n>")):
    if i !=' ':
        list1.append(alf[i])
print(" ".join(list1))
# alf_reverse = pd.Series(alf_russ, index=[to10_2(i+1) for i in range(len(alf_russ))])
# for i in list1:
#     print(alf_reverse[str(i)])
