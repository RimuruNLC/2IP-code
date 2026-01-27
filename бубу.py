def zadacha12():
    str_polz = str(input("Введите строку в которой есть # - "))
    list_polz = list(str_polz)
    list_polz.reverse()
    count_polz = 0
    for i in range(len(list_polz)):
        if list_polz[i] == "#":
            break
        else:
            count_polz += 1
    print(count_polz)
def zadacha13():
    str_polz = str(input("Введите любую строку на английском - "))
    list_polz = list(str_polz)
    count_abc = 0
    for i in range(len(list_polz)):
        if list_polz[i] == "a" and list_polz[i+1] == "b" and list_polz[i+2] == "c":
            count_abc += 1
    print(count_abc)
def zadacha14():
    str_polz = str(input("введите строку имеющую : - "))
    list_polz = list(str_polz)
    count_replace = 0
    for i in range(len(list_polz)):
        if list_polz[i] == ":":
            list_polz[i] = ";"
            count_replace += 1
    str_polz = "".join(list_polz)
    print(str_polz,count_replace)
def zadacha16():
    str_polz = str(input("введите строку содержащую скобки - "))
    list_polz = list(str_polz)
    index_one = list_polz.index("(")
    index_two = list_polz.index(")")
    list_finam = []
    for i in range(len(list_polz)):
        if i < index_one or i > index_two:
            list_finam.append(list_polz[i])
    str_finam = "".join(list_finam)
    print(str_finam)
def zadacha17():
    perecluch=False
    str_polz = str(input("Строка пользавателя с $ - "))
    chetchic_false = 0
    chetchic_true = 0
    for i in str_polz:
        if perecluch == False:
            if i != "$":
                chetchic_false += 1
            else:
                perecluch = True
        else:
            chetchic_true += 1
    print(f"До $ - {chetchic_false},после $ - {chetchic_true}")

def zadacha18():
    str_polz = str(input("строка пользавателя - "))
    liss_final = []
    for i in range(len(str_polz)):
        chetchic_false = 0
        for j in range(len(str_polz)):
            if str_polz[i] == str_polz[j]:
                chetchic_false += 1
        if chetchic_false == 1:
            liss_final.append(str_polz[i])
    str_final = "".join(liss_final)
    print(str_final)


