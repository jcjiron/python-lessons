class Order:
    def __init__(self, order_id, lines):
        self.order_id = order_id
        self.lines = lines

    def __eq__(self, other):
        return isinstance(other, Order) and self.order_id == other.order_id
