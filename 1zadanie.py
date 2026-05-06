import numpy as np
def zadacha2():
    def proverk(a):
        list2 = [int(i) for i in str(a) if int(i)%2==0]
        if sum(list2) != 0:
            return sum(list2)
        return 2

    while True:
        a = str(input(">"))
        list1 = a.split(" ")
        if len(list1) != 2 or int(list1[0]) < 0  or int(list1[1])>30000:
            print("Введите снова")
        else:
            for i in range(int(list1[1]), int(list1[0]),-1):
                if proverk(i)%3==0:
                    print(i)
                    break
            break

zadacha2()
def zadacha3():
    list_final = []
    def umn(n):
        return int(n[:1]) * int(n[1:])
    def proverk(a):
        chet = 0
        for i in a:
            for j in a:
                if umn(i) == umn(j):
                    chet += 1
                else:
                    list_final.append(chet)
                    chet = 0
                    continue
            list_final.append(chet)
    while True:
        a = str(input(">"))
        list_chisla = a.split(" ")
        if int(list_chisla[0]) != len(list_chisla)-1 or int(list_chisla[0])>1000:
            print("Введите снова")
        else:
            list_chisla.pop(0)
            proverk(list_chisla)
            print(max(list_final))
            break
list_nvc = [31,28,31,30,31,30,31,31,30,31,30,31]
list_vc = [31,29,31,30,31,30,31,31,30,31,30,31]
list1 = str(input("введите дату и число дд мм гггг \n>")).split(" ")
den = list1[0]
mesaz = list1[1]
god = list1[2]
dennd = 0
for i in range(int(den)):
    dennd+=1
for i in range(0,int(mesaz)-1):
    if int(god)%4 == 0:
        dennd+=list_vc[i]
    else:
        dennd+=list_nvc[i]
a = int(list1[3])-1
for i in range(dennd):
    if a == 7:
        a = 0
    a+=1
print(a)
