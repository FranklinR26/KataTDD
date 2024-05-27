import unittest
from SRC.logica.Conjunto import  Conjunto

class TestConjunto(unittest.TestCase):
    def test_Conjunto_vacio_retornable(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])

        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])

        self.assertEqual(5, conjunto.promedio())

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_conjunto_dosElementos_retornaPromedioElementos(self):
        conjunto = Conjunto([5, 7])

        self.assertEqual(6, conjunto.promedio())


if __name__ == '__main__':
    unittest.main()
