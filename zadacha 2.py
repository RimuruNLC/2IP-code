# for i in range(1,4):
# #     for j in range (1,4):
# #         print(i,j, sep=" -()-()- ")
h=0
k='#'
for i in range(1,4):
    for j in range (1,4):
        if j == 2 and i == 2 or i == j - 2 or i == j + 2:
           print(k, end=' ')
        elif j == i:
           print(k, end=' ')
        else:
            print(h,end=' ')
    print(end="\n")
