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
