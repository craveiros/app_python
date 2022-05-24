"""

Uma entrada de valores numéricos (uma lista deles)

0 - 75.00 -> 0%
75.01 - 150.00 -> 10%
150.01 - 300.00 -> 20%
300.01 -> 25%

"""

import unittest
from app2 import percentual_desconto

# Importing os module
import os

class TestePercentualDeDesconto(unittest.TestCase):
   # def teste_exite_percentualdedesconto(self):
   #     percentual_desconto()

    def teste_percentual_desconto_deve_retornar_0_quando_input_for_0_75(self):
        """percentual_desconto(0 - 75.00) -> '0%'"""
        import os
        print(os.environ['DESCONTO_INTERVALO_1'])
        valor_esperado = os.environ['DESCONTO_INTERVALO_1']

        valor_de_compra = 45
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 75.00
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 75.01
        self.assertNotEqual(percentual_desconto(valor_de_compra), valor_esperado)

    def teste_percentual_desconto_deve_retornar_10_quando_input_for_75_150(self):
        """percentual_desconto(75.01 - 150.00) -> '10%'"""
        import os
        print(os.environ.get('DESCONTO_INTERVALO_2'))
        valor_esperado = os.environ['DESCONTO_INTERVALO_2']

        valor_de_compra = 90
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 75.00
        self.assertNotEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 75.01
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 150.00
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 150.01
        self.assertNotEqual(percentual_desconto(valor_de_compra), valor_esperado)

    def teste_percentual_desconto_deve_retornar_10_quando_input_for_150_300(self):
        """percentual_desconto(150.01 - 300.00) -> '20%'"""
        import os
        print(os.environ.get('DESCONTO_INTERVALO_3'))
        valor_esperado = os.environ['DESCONTO_INTERVALO_3']

        valor_de_compra = 225
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 150.00
        self.assertNotEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 150.01
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 300.00
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 300.01
        self.assertNotEqual(percentual_desconto(valor_de_compra), valor_esperado)

    def teste_percentual_desconto_deve_retornar_25_quando_input_for_300(self):
        """"percentual_desconto(300.01) -> '25%'"""
        import os
        print(os.environ.get('DESCONTO_INTERVALO_4'))
        valor_esperado = os.environ['DESCONTO_INTERVALO_4']

        valor_de_compra = 690.00
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 300.00
        self.assertNotEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = 300.01
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

        valor_de_compra = float('inf')
        self.assertEqual(percentual_desconto(valor_de_compra), valor_esperado)

if __name__ == '__main__': unittest.main()

