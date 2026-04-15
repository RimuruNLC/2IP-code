import pandas as pd
kredits = [2000000,20000,20000000]
procent = [20, 26, 22]
summ = 0
data = ['09.05.26', '09.06.26', '09.07.26', '09.08.26', '09.09.26', '09.10.26', '09.11.26', '09.12.26', '09.01.27', '09.02.27', '09.03.27', '09.04.27']
list1 = []
for _ in range(12):
    for i in range(3):
        summ += kredits[i] * (procent[i]*0.01)/12
    summ-= summ*0.15/12
    list1.append(int(summ))
a = {
    "Месяц":[i for i in data],
    "Счет банка":[i for i in list1]
}
tablica = pd.DataFrame(a)
print(tablica)
