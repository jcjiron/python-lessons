from order import Order


class OrderBuilder:
    def __init__(self):
        self._items = []

    def add_item(self, product, quantity):
        self._items.append((product, quantity))
        return self

    def build(self):
        return Order(self._items)
