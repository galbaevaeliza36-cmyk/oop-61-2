#Инкапцуляция
# public-обычные отрибуты
#_protected-одно почеркивание :"не трогой,это внутреннее"
#__private-два подчеркивание :"работает name-manglic (настоящее скрытие)

class BankAkaunt:
    def __init__(self,name,balans,password):
        self.name = name #это у нас отрибуты
        self._balans = balans
        self.__password = password
    # def get_balans(self):
    #     return self.__balans
    def get_balans(self,password):
        if password == self.__password:
            return self._balans
        else:
            return ("не верный пороль")


Eliza = BankAkaunt ("Eliza",500,"eli0508") #это экземпяр класса
# print (Eliza.name) #через точку мы обращяемся к отрибутом
# print (Eliza._balans)
# print (Eliza.__password)
print (Eliza.get_balans("eli05"))

