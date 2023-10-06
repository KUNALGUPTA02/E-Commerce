class DiscountStrategy:
    def apply_discount(self, price):
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage #percentage discount which is offer by company

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)


