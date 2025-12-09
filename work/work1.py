#1
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою! "


# 2
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"{self.name} кастует заклинание {self.mp}!"


class WarriorHero(MageHero):
    def action(self):
        return f"{self.name} рубит мечом {self.lvl}"


Aki = MageHero("Aki", 5, 100, 50)
Miki = WarriorHero("Miki", 100, 102, 70)

# 3
class BankAccount:
    bank_name = "optima"

    def __init__(self, hero, lvl, balance, password):
        self.hero = hero
        self.lvl = lvl
        self._balance = balance
        self.__password = password

    # 4
    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return f"Герой: {self.hero.name}, уровень: {self.hero.lvl}, баланс: {self._balance}"

    @staticmethod
    def get_bank_name():
        return BankAccount.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) != type(other.hero):
            raise ValueError("Нельзя складывать счета героев разных классов")
        return self._balance + other._balance

    def __eq__(self, other):
        return (
            self.hero.name == other.hero.name and
            self.hero.lvl == other.hero.lvl
        )


# 5
from abc import ABC, abstractmethod


class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        return f'<text>Код: 1234</text><phone>{phone}</phone>'


class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}


# === ТЕСТ ===
mage1 = MageHero("Aki", 20, 500, 100)
mage2 = MageHero("Ari", 80, 500, 200)
warrior = WarriorHero("Miki", 50, 900, 20)

acc1 = BankAccount(mage1, 'optima', 2000, "Opti0507")
acc2 = BankAccount(mage2, 'optima', 3000, "0506")
acc3 = BankAccount(warrior, 'optima', 2500, "2536")

print(mage1.action())
print(warrior.action())

print(acc1)
print(acc2)

# --- Классовые и статические методы ---
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

# --- Магические методы: __add__ ---
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

try:
    print("Сумма мага и воина:", acc1 + acc3)
except Exception as e:
    print("Ошибка:", e)

# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

# --- SMS ---
sms = KGSms()
print(sms.send_otp("+996777123456"))