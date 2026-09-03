import unittest

from pedido_builder import PedidoBuilder
from producto import Producto


class TestPedidoBuilder(unittest.TestCase):
    def test_build_regresa_pedido_con_los_items_agregados(self):
        playera = Producto("playera", precio=250)
        gorra = Producto("gorra", precio=150)

        pedido = (
            PedidoBuilder()
            .agregar_item(playera, cantidad=2)
            .agregar_item(gorra, cantidad=1)
            .build()
        )

        self.assertEqual(pedido.items, [(playera, 2), (gorra, 1)])


if __name__ == "__main__":
    unittest.main()
