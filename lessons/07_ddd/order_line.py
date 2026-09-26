from money import Money


class OrderLine:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @property
    def subtotal(self):
        return Money(self.product.price * self.quantity)
