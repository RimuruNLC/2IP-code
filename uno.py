import random
uno_list = [0,1,2,3,4,5,6,7,8,9,"Блок","Реверс", "+4карты и выбор цвета"]
svet_list = ["Желтый","Красный","Синий","Зеленый","Безцветный"]
stol_list=[]
class Uno:
    def __init__(self):
        self.invertary = []
        for i in range(6):
            uno_index = random.randint(0,12)
            svet_index = random.randint(0,4)
            if uno_index == 12:
                self.invertary.append([uno_index,4])
            else:
                self.invertary.append([uno_index, svet_index])
    def see_invertary(self):
        print(f"Ваши карты! Их общее кол-во {len(self.invertary)}")
        for i in self.invertary:
            print(uno_list[i[0]], svet_list[i[1]], sep = '\t|\t')
    def __iadd__(self, other):
        for i in range(other):
            uno_index = random.randint(0,12)
            svet_index = random.randint(0,4)
            self.invertary.append([uno_index,svet_index])
        return self
    def __len__(self):
        return len(self.invertary)
    def __le__(self, other):
        return len(self.invertary) <= other
    def __eq__(self, other):
        return len(self.invertary) == other
    def sbros_karti(self):
        print(f"Ваши карты! Их общее кол-во {len(self.invertary)}")
        x = 0
        for i in self.invertary:
            print(x, uno_list[i[0]], svet_list[i[1]], sep='\t|\t')
            x += 1
        index = int(input("Выберите какую карту вы хотите сбросить. - "))
        s = self.invertary.pop(index)
        stol_list.insert(0,s)

    def sbros_karti_bot(self):
        x = random.randint(1, len(self.invertary))
        s = self.invertary.pop(x)
        stol_list.insert(0,s)

    @staticmethod
    def see_stol():
        print(f"Карты стола! Их общее кол-во {len(stol_list)}")
        for i in stol_list:
            print(uno_list[i[0]], svet_list[i[1]], sep='\t|\t')
def proverk(igrok):
    if igrok == 0:
        return True
    elif igrok >=1:
        return False

x = False
igrok1 = Uno()
igrok2 = Uno()
igrok3 = Uno()
def hod_igrok(igrok):
    while True:
        a = int(input("Выберите действие которое вы хотите сделать \n Доступные действия: \n1 - посмотреть инвертарь\n2 - сделать ход\n3 - сказать УНО\n> "))
        if a == 1:
            igrok.see_invertary()
        elif a == 2:
            igrok.sbros_karti()
            break
        elif a == 3:
            print("Вы сказали уно!")
            if igrok == 1:
                print("Молодец, вы успели сказать уно")
            else:
                print("Вы не успели, или действие было лишним! Берете две карты")
                igrok+=2

        else:
            print("Такого действия нет!")
def hod_bot(igrok):
    igrok.sbros_karti_bot()
while x == False:
    hod_igrok(igrok1)
    hod_bot(igrok2)
    hod_bot(igrok3)
    Uno.see_stol()
