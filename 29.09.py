# list1 = []
# print(list1)
# print(type(list1))
#
# list2 = [1,2,3,4,5,6,7,8,9,10]
# # print(list2)
# # print(list2[1] + list2[2])
# for i in range(5):
#     print(list2[i])
#
# print(5*'-')
#
# j=0
# while j<5:
#     print(list2[j])
#     j+=1
#
# print('*'*10)
#
# list3=list()
# print(list3)
# print('*'*10)
#
# list4 = [4,'ser', True,34,67,'wer','rtt']
# print(list4[2])
#
# print('*'*5)
#
# for k in range(7):
#     print(list4[k])
#
# print('*'*5)
# str1 = 'hello world'
# print(str1)
#
# list5 = list(str1)
# print(list5)
# list7=[i for i in range(15)]
# list7.reverse()
# print(list7)
# print(sum(list7))
# print(len(list7))


list1 = [22,23,25,26,27]
print(list1)

print(10*'_', '\n')

for r in range(len(list1)):
    if list1[r]!= 25:
        print(list1[r])

print(10*'_', '\n')

x = 0
for i in range(len(list1)):
    x= x+list1[i]
print(x)
