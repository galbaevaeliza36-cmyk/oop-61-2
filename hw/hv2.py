class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def info(self):
        return f"{self.name}, {self.age} лет, вес {self.weight}"

    def use_ability(self):
        return f"{self.name} использует базовую способность. "


class PetAnimal(Animal):
    def action(self):
        return f"{self.name} hi!!"

    def eat(self):
        return f"{self.name} может летать !!!"


class WerriorAnimal(PetAnimal):
    def attack(self):
        return f"{self.name} наносит удар током!!!"


# ===== МИКСИНЫ =====
class Runable:
    def use_ability(self):
        return super().use_ability() + "бегает. "


class Shootable:
    def use_ability(self):
        return super().use_ability() + "стреляет лазером. "


class Flyable:
    def use_ability(self):
        return super().use_ability() + "летает. "


class Swimmable:
    def use_ability(self):
        return super().use_ability() + "плавает. "


# ===== ЖИВОТНЫЕ =====
class Dog(Runable, Swimmable, Animal):
    pass


class Rabbit(Flyable, Shootable, Animal):
    pass


class Phoenix(Flyable, Shootable, Animal):
    def reborn(self):
        return f"{self.name} восстал из пепла!"


# ===== ЗООПАРК =====
class Zoo:
    def __init__(self):
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def show_all(self):
        for a in self.animals:
            print(a.info())

    def perform_show(self):
        for a in self.animals:
            print(a.use_ability())


# ===== MAIN BLOCK =====
if __name__ == "__main__":
    zoo = Zoo()

    dog = Dog("miko", 2, 20)
    rabbit = Rabbit("erik", 5, 20)

    for animal in (dog, rabbit):
        zoo.add_animal(animal)

    print("=== Информация о животных ===")
    zoo.show_all()

    print("\n=== Шоу суперспособностей ===")
    zoo.perform_show()

    print("\nMRO для Dog:", Dog.__mro__)
    print("MRO для Rabbit:", Rabbit.__mro__)















































































