class Product:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Laptop(Product):
    pass


class Headphones(Product):
    pass
