import sys
import os
# # print(sys.version)
# # print(sys.platform)
# # sys.stdout.write(sys.platform)
# # sys.stderr
# myfile = open("hello.txt", "a")
# # myfile.write("Строка ")
# # print("test", file=myfile)
# # myfile.write("ууу")
# myfile.close()
# f = open("hello.txt", "r")
# # print(f.read())
# print(f.readline(3))
# f.close()



if not os.path.exists("D:\\python2IP\\uroki(data)\\111"):
    os.mkdir("111")
    os.chdir("111")
    myfile = open("test.txt", "a")
    print("hello, world", file=myfile)
    myfile.close()
    os.chdir("D:\\python2IP\\uroki(data)")
if not os.path.exists("D:\\python2IP\\uroki(data)\\222"):
    os.mkdir("222")
    os.rename("D:\\python2IP\\uroki(data)\\111\\test.txt","D:\\python2IP\\uroki(data)\\222\\test.txt")
    os.chdir("222")
    myfile2 = open("test.txt","a")
    print("\nHello, Тимофей и Евгений", file=myfile2)
    myfile2.close()
    myfile3= open("test.txt","r")
    print(myfile3.read())
    myfile3.close()



