class Phone:
    __SECRET_CODE = "Eli0206"
    def __init__(self,name,price,discount,):
        self.name = name
        self._price = price
        self.__discount = 0
        self.__extra_discount = 0
    def get_price(self):
        price_after_discount = self._price * (1 - self.__discount / 100)
        final_price = price_after_discount * (1 - self.__extra_discount / 100)

        return (final_price)
    def get_discount(self,percent):
        if 0 <= percent <= 50:
            self.__discount = percent
        else:
             return "Ошибка: скидка не может превышать 50%"

    def apply_extra_discount(self, secret_code):
        if secret_code == self.__SECRET_CODE:
            self.__extra_discount = 5
        else:
            return "Неверный код"

iphone = Phone("iphone", 20000,20)
iphone.get_discount(20)
print(iphone.apply_extra_discount("Eli0206"))
print(iphone.get_price())