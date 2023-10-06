import copy

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity=1):
        for _ in range(quantity):
            self.cart_items.append(copy.deepcopy(product))

    def remove_from_cart(self, product, quantity=1):
        cart_copy = self.cart_items.copy()  # copy to iterate over
        for item in cart_copy:
            if item.name == product.name and quantity > 0:
                self.cart_items.remove(item)
                quantity -= 1
            elif item.name == product.name and quantity <= 0:
                break



    def update_quantity(self, product, quantity):
        self.add_to_cart(product, quantity)


class ShoppingCart:
    def __init__(self, discount_strategy=None):
        self.cart = Cart()
        self.discount_strategy = discount_strategy

    def calculate_total_bill(self):
        total_bill = sum(item.price for item in self.cart.cart_items)
        if self.discount_strategy:
            total_bill = self.discount_strategy.apply_discount(total_bill)
        return total_bill
