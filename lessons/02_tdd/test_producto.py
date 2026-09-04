import unittest

from producto import Producto


class TestProducto(unittest.TestCase):
    def test_guarda_nombre_y_precio(self):
        producto = Producto("playera", precio=250)

        self.assertEqual(producto.nombre, "playera")
        self.assertEqual(producto.precio, 250)


if __name__ == "__main__":
    unittest.main()
