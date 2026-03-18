if int(input("1 - Из двоичной в десятичной\n2 - Из десятичной в двоичной\n>")) == 1:
    list1 = list(str(input("Введите двоичное число\n>")))
    list1.reverse()
    x=0
    int_final = 0
    for i in list1:
        int_final+=(int(i)*2**x)
        x+=1
    print(int_final)
else:
    str_final = ""
    int10 = int(input("Введите число в десятичной системе\n>"))
    while int10 != 0:
        str_final += str(int10%2)
        int10//=2
    print(str_final)
