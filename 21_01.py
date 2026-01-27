



class Mag:
    def __init__(self,health_point,count_mana, cast_damage,lvl,name,zelie_health=0,zelie_mana=0):
        self.lvl = lvl
        self.health_point=health_point
        self.health_point -= (lvl*0.5)
        self.count_mana = count_mana
        self.count_mana -=(lvl*2)
        self.cast_damage =cast_damage
        self.cast_damage -=(lvl*0.5)
        self.name = str(name)
        self.zelie_health= zelie_health
        self.zelie_mana=zelie_mana
    def healing(self,name):
        if self.count_mana >= 10:
            self.count_mana-=10
            name.health_point+=self.cast_damage
            print('заклинание сработало')
        else:
            print("маны нет.")

    def fair_b(self,name):
        if self.count_mana >= 15:
            self.count_mana-=15
            name.health_point -= self.cast_damage
            print('заклинание сработало')
        else:
            print("маны нет.")
    def invertar(self,x):
        if x == 1:
            print(f" зелья здоровья : {self.zelie_health} зелья маны : {self.zelie_mana}")
        if x == 2:
            if self.zelie_health >=1:
                self.health_point += 15
                self.zelie_health -= 1
            else:
                print("Нету зелек!")
        if x == 3:
            if self.zelie_mana >=1:
                self.count_mana += 15
                self.zelie_mana -= 1
            else:
                print("Нету зелек!")





class Voin:
    def __init__(self,health_point,energy, cast_damage,lvl,name,zelie_health=0,zelie_mana=0):
        self.lvl = lvl
        self.health_point = health_point
        self.health_point -= (lvl * 0.5)
        self.energy = energy
        self.energy += (lvl * 2)
        self.cast_damage = cast_damage
        self.cast_damage -= (lvl * 0.5)
        self.name = str(name)
        self.zelie_health= zelie_health
        self.zelie_mana=zelie_mana

    def hit(self,name):
        if self.energy >= 15:
            self.energy-=15
            name.health_point -= self.cast_damage
            print('ударил')
        else:
            print("нет силы.")

    def invertar(self, x):
        if x == 1:
            print(f" зелья здоровья : {self.zelie_health} зелья маны : {self.zelie_mana}")
        if x == 2:
            if self.zelie_health >= 1:
                self.health_point += 15
                self.zelie_health -= 1
            else:
                print("Нету зелек!")
        if x == 3:
            if self.zelie_mana >= 1:
                self.energy += 15
                self.zelie_mana -= 1
            else:
                print("Нету зелек!")


ralsei = Mag(100,100,10,5,"Ральзеи")

ralsei_goner = Mag(100,100,10,2,"Ральзеи доходяга")

def create_sosud():
    print('ПРИВЕТСТВУЮ ТЕБЯ..')
    print("СОЗДАЙ СОСУД ")
    k = input(" МАГ - 1 \n ВОИН - 2 \n КАКОЙ КЛАСС - ")

    

# x = input("\n кого хочешь фаербольнуть")
# if x == 1:
#     ralsei.fair_b(ralsei_goner)