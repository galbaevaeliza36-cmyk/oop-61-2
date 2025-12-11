class Product:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} - {self.price}сом, в наличии: {self.quantity}"

    def __repr__(self):
        return f"Product(title={self.title!r}, price={self.price!r}, quantity={self.quantity!r})"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.title == other.title
        return False

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Product):
            total_price = self.price + other.price
            return Product("Combo", total_price, 1)
        return NotImplemented


# Пример использования:
p1 = Product("Клавиатура", 1500, 10)
p2 = Product("Клавиатура", 1800, 5)
p3 = Product("Мышка", 700, 20)

print(p1 == p2)      # True (название одинаковое)
print(p3 < p1)       # True (700 < 1500)
combo = p1 + p3
print(combo)         # Product(title="Combo", price=2200, quantity=1)
print(str(combo))    # Combo - 2200₽, в наличии: 1
print(repr(combo))   # Product(title='Combo', price=2200, quantity=1)