class Hero:
    def __init__(self, name,lvl,hp):
        self.name = name
        self.lvl=lvl
        self.hp=hp
    def action(self):
        return f"{self.name} готов к бою! "
class MageHero(Hero):
    def __init__(self, name,lvl,hp,mp):
        super(). __init__(name,lvl,hp)
        self.mp=mp
    def action (self):
        return f"{self.name} кастует заклинание {self.mp}!"

class WarriorHero(MageHero):
    def action (self):
        return f"{self.name}рубит мечом {self.lvl}"
Aki=MageHero("Aki",5,100,50)
Miki=WarriorHero("Miki",100,102,70)

class BankAccount:
    def __init__(self,hero,balance,password):
        self.hero=hero
        self._balance=balance
        self.__password=password

    def get_balance(self, password):
        if password == self.__password:
            return self._balance
        return 'не верный пароль'

    # def full_info (self):


Optima=BankAccount("Optima",5000,"Opti0507")

class Bank:
    def __init__(self,hero,balance):
        self.hero=hero
        self._balance=balance
    def __add__(v2,v1):
        if type(v2)==type(v1):
            print (v2.n+v1.n)
        else:
            print ("ошибка")

v1=Bank(Optima,5000)
v2=Bank(Optima,2500)

