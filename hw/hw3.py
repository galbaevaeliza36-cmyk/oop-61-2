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




from abc import ABC, abstractmethod


# Абстрактный класс
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


# Реализации способов оплаты
class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")

    def refund(self, amount):
        print(f"Возврат на карту: {amount}")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")

    def refund(self, amount):
        print(f"Возврат наличными: {amount}")


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print({"type": "crypto", "amount": amount, "currency": "USDT"})

    def refund(self, amount):
        print({"refund": True, "amount": amount, "currency": "USDT"})


# Класс PaymentProcessor
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount):
        self.payment_method.pay(amount)


# Примеры вызовов
processor = PaymentProcessor(CardPayment())
processor.process(100)

processor = PaymentProcessor(CashPayment())
processor.process(50)

processor = PaymentProcessor(CryptoPayment())
processor.process(200)