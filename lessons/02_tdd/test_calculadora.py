import unittest

from calculadora import calcular_total
from pedido_builder import PedidoBuilder
from producto import Producto


class TestCalculadora(unittest.TestCase):
    def test_suma_items_sin_descuento(self):
        gorra = Producto("gorra", precio=150)
        pedido = PedidoBuilder().agregar_item(gorra, cantidad=1).build()

        self.assertEqual(calcular_total(pedido), 150)

    def test_aplica_10_por_ciento_si_supera_500(self):
        playera = Producto("playera", precio=250)
        pedido = PedidoBuilder().agregar_item(playera, cantidad=3).build()

        self.assertEqual(calcular_total(pedido), 675)

    def test_aplica_cupon_descuento10_y_luego_regla_de_orden_grande(self):
        playera = Producto("playera", precio=250)
        gorra = Producto("gorra", precio=150)
        pedido = (
            PedidoBuilder()
            .agregar_item(playera, cantidad=2)
            .agregar_item(gorra, cantidad=1)
            .build()
        )

        self.assertEqual(calcular_total(pedido, cupon="DESCUENTO10"), 526.5)


if __name__ == "__main__":
    unittest.main()
