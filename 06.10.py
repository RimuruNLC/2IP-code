# list1=[1,2,3,4,5]
# tuple1 = tuple(list1)
# print(tuple1)
# print(tuple1[2])
# tuple3 = tuple([1,2,3,4,5])
# print(tuple3)
# tuple4 = 1,2,3,4,5
# print(tuple4)
# a,b,c,v,z = tuple4
# print(a)
# tuple5 = 4,
# print(tuple5)
# tuple1=(1,2,3,4,5)
# list1= list(tuple1)
# print(list1)
# list1.append(23)
# print(list1)
# tuple2 = tuple(list1)
# print(tuple2)
# db_connect = ("host","root",123)

# print(db_connect)
# del db_connect
# db_connect = ("host","root",123,12,23,634,2,34,465,76)
# print(len(db_connect))
# tuple2=(2,)
# tuple3= db_connect + tuple2
# print(tuple3)


# tuple1 = tuple([1,2,3])
# tuple2 = (1, 2, 3)
# if tuple1 == tuple2:
#     print('da')

#
# list0 = [ ]
# list0.append(int(input(" список :")))
# print(list0)


# tuple1=()
# print(tuple1)
# while True:
#     user_numb = int(input("e,worgiphr:"))
#     list1=list(tuple1)
#     list1.append(user_numb)
#     tuple1=tuple(list1)
#     print(tuple1)
# t1=2,3,4,5,6
# for i in range(4):
#     t2=tuple((input("число введи - ")))
#     t1 = t1 + t2
#     print(t1)

list1 = ['1',',', '2', ',', '3']
tuple1 = []
print(list1)
for i in list1:
    if i == '1' or i == '2' or i == '3':
        list2 = list(tuple1)
        list2.append(int(i))
        tuple1 = tuple(list2)
print(tuple1)