# s = int(input('Ведите последнее число: '))
# c = int(input('Ведите первое число: '))
#
# while 0 <= s:
#     print(c)
#     c += 1
#     if c > s:
#         break



a = int(input('Введите число a = '))
b = int(input('Введите число b = '))
c = 0
i = 1
while i <= a:
    if i == b:
        i += 1
        continue
    print (i)
    c = c + i
    i+=1
print("сумма всех чисел в ряду:", c)


