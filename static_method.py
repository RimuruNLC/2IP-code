# import random
# import time
#
# class Pogida:
#     def __init__(self, temp, vlajnost):
#         self.temp = temp
#         self.vlajnost = vlajnost
#     @staticmethod
#     def luboe_deystvie():
#         print("Испытаем твою удачу! Бросим кубик")
#         a = random.randint(1, 6)
#         print(a)
#     @staticmethod
#     def get_time():
#         return time.ctime(time.time())
# Pogida.luboe_deystvie()
# print("Статические методы можно вызывать не создавая обьект класса, делая работу с ним удобнее")
# print(Pogida.get_time())
# print("Таким образом можно создавать удобные фукнции облегчающие работу с классом или чем либо еще!")
# print("Но при этом мы не можем работать с свойствами или характеристиками класса, т.к. обьект не создан, и бла бла бла..")
# print(":(")
#


class Chto_to:             #создаем любой класс
    def __init__(self):    #добавляем его характеристики (необяз)
        pass
    @staticmethod          # обьявляем статический метод, для следующей функции
    def prostoe_deystvie(): #делаем тот самый метод
        print(2+2)            # Да.
Chto_to.prostoe_deystvie() # вызываем это действие








