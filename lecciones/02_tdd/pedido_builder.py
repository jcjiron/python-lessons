from pedido import Pedido


class PedidoBuilder:
    def __init__(self):
        self._items = []

    def agregar_item(self, producto, cantidad):
        self._items.append((producto, cantidad))
        return self

    def build(self):
        return Pedido(self._items)
