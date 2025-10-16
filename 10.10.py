# set1 = {1,2,3,3,3,3,4,5}
# print(set1)
# print(type(set1))
# list1 = [1,2,3,3,3,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2]
# set2 = set(list1)
# print(set2)
#
# list2 = ['h','h','e','l','l','l','o','w','o','r','l','l','d',]
# print(list2)
# set3 = set(list2)
# print(set3)
# s = 0
# set3 = {5,6,4,7,5}
# print(set3)
# for i in set3:
#     print(i)
#     s+=i
# print(s)
# for i in set3:
#     if type(i) == int:
#         print(i)
# set3.add(45)
# print(set3)
# set3.remove(1)
# print(set3)

# set1 = {4, 5, 6, 7, 89, 10}
# set2= {8,9}
# set1.remove(89)
# set1.update(set2)
# print(set1)
# set3 = {0}
# for i in range(5):
#     a = int(input("Введите число - "))
#     set3.add(a)
# set3.remove(0)
# print(set3)


# list1=[]
# set1=set()
# for i in range(5):
#     a = int(input('Введите число - '))
#     if a % 2 == 0:
#         list1.append(a)
#     else:
#         set1.add(a)
# print("четные числа - ", list1)
# print("нечетные числа - ", set1)

# print('  o \n /|\\ \n /\\')

#
# set1 = {i for i in range(5)}
# print(set1)
#
# dict1 = {"key" + str(i): i for i in range(5)}
# print(dict1)
# # tuple1 = (int(i) for i in range(5))
# # print(tuple1)
# list1=[i for i in range(1000)]
# print(list1)


list1 = [i for i in range(10) if i%2 != 0]
print(list1)
list1