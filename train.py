import random
massive = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
while True:
    def tabl():
        for i in range(3):
            print("\n")
            for j in range(3):
                print(massive[i][j], end="\t")
        print("\n")

    def krest():
        while True:
            a = random.randint(0,2)
            b = random.randint(0, 2)
            if massive[a][b] == "-":
                massive[a][b] = "X"
                break
            else:
                continue
    def noliki():
        while True:
            a = int(input("Введите номер строки(0-2) - "))
            b = int(input("Введите номер (0-2) - "))
            if massive[a][b] == "X" or massive[a][b] == "O":
                print("Эта клетка уже занята!")
            else:
                massive[a][b] = "O"
                break
    def chet(a):
        for i in range(3):
            chetchic = 0
            for j in range(3):
                if massive[i][j] == str(a):
                    chetchic += 1
                if chetchic == 3:
                    print(f"Победил {a}!")
                    return True
        for n in range(3):
            chetchic1 = 0
            for m in range(3):
                if massive[m][n] == str(a):
                    chetchic1 += 1
                if chetchic1 == 3:
                    print(f"Победил {a}!")
                    return True
        for i1 in range(3):
            chetchic2 = 0
            if massive[i1][i1] == str(a):
                chetchic2 += 1
            if chetchic2 == 3:
                print(f"Победил {a}!")
                return True
        if massive[0][2] == str(a) and massive[1][1] == str(a) and massive[2][0] == str(a):
            print(f"Победил {a}!")
            return True



    krest()
    tabl()
    if chet("X") == True:
        break
    noliki()
    tabl()
    if chet("O") == True:
        break
