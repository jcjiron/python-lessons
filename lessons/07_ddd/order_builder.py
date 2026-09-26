from order import Order
from order_line import OrderLine


class OrderBuilder:
    def __init__(self, order_id):
        self.order_id = order_id
        self._lines = []

    def add_item(self, product, quantity):
        self._lines.append(OrderLine(product, quantity))
        return self

    def build(self):
        return Order(self.order_id, self._lines)
