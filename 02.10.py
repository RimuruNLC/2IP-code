# list1 = [1,True,2,"x",'eret',-237,'list1',3-77,'Hello World',4,-200,':-)','index',]
# list3 = list1.copy()
#
# # 1. Создать отсортированный по возрастанию числовой массив
# # 2. Все строковые элементы собрать в отдельный список
# # 3.Найти максимальый и минимальный элементы из числового массива
# # 4. Удалить максимальный, вытолкунть минимальный
#
# list2 = []
# a = list1.pop(0)
# print(a)
# list2.append(a)
# print(list2)
# a = list1.pop(1)
# list2.append(a)
# print(list1)
# print(list2)
# print(list1)
#
# list2.append(list1.pop(3))
# print(list1)
# print(list2)
# list2.append(list1.pop(4))
# print(list1)
# print(list2)
# list2.append(list1.pop(-4))
# print(list1)
# print(list2)
# list2.append(list1.pop(-3))
# print(list1)
# print(list2)
# list2.sort()
# print(list2)
#
# list1.remove(True)
# print(list1)
#
# print(min(list2))
# print(max(list2))
#
# list2.remove(min(list2))
# print(list2)
#
# s = list2.pop(-1)
# print(s)
# print(list2)
# list1 = [1 ,2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# list3 = []
# x=0
# while x < 5:
#     a = list1.pop(0)
#     b = list2.pop(0)
#     list3.append(a)
#     list3.append(b)
#     x+=1
# print(list3)

# list1 = [1, 2, 'we', 3, 'wer', 4, 5, 6, 'sad',7]
# # Найти сумму чисел
# x = 0
# for i in list1:
#     if type(i) == int:
#         x+=i
# print(x)
list1 = [1, True,2,"x",'eret',-2,'list1',2.5, False ,3-77,'Hello World',4,-7,':-)',4.5,'index']
x = 0
b = 0
str1 = 0
count_x=0
count_b=0
list2 = []
list3 = []
list_copy=list1.copy()
list_int=[]
list_float=[]
list_bool=[]
list_str = []
for k in list_copy:
    if type(k)==int:
        list_int.append(k)
    if type(k)==float:
        list_float.append(k)
    if type(k)==bool:
        list_bool.append(k)
    if type(k)==str:
        list_str.append(k)
for i in list1:

    if type(i) == float:
        b += i
        count_b+=1
    if type(i) == int:
        x += i
        count_x +=1
    if type(i) == bool:
        h = list1.pop(i)
        list2.append(h)
    if type(i) == str:
        str1 += 1


print('сумма целых чисел = ',x, ' Количество целых чисел =', count_x)
print('сумма дробных чисел = ',b, ' Количество дробных чисел =', count_b)
print('кол-во bool-обьектов',len(list2))
print('кол-во строковых обьектов:', str1)
print(list_int)
print(list_float)
print(list_bool)
print(list_str)
# Найти сумму чисел
# Найти количекство целых числ, вещественных чисел
# Найти количество логических значений
# Найти количество строковых значений
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 = [3, 4, 'b']
# x=0
# v=0
# print(list1)
# print(list2)
# for i in list3:
#     for c in list1:
#         if c == i:
#             list1.remove(i)
#     for n in list2:
#         if n == i:
#             list2.remove(i)
# print(list1)
# print(list2)
# while x < 3:
#     a = list3.pop()
#     while v < 5:
#         b = list1