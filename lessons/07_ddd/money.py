class Money:
    def __init__(self, amount):
        self.amount = round(amount, 2)

    def __eq__(self, other):
        return isinstance(other, Money) and self.amount == other.amount

    def __repr__(self):
        return f"Money({self.amount})"

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def apply_discount(self, fraction):
        return Money(self.amount * (1 - fraction))
