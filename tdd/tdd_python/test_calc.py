"""

Uma entrada de valores numéricos (uma lista deles)

0 - 50.00 -> 0%
50.01 - 100.00 -> 5%
100.01 - 150.00 -> 10%
150.00 - 250.00 -> 15%
250.00 -> 20%

"""

from unittest import TestCase, main
from app import percentual_desconto

class TestePercentualDeDesconto(TestCase):
   # def teste_exite_percentualdedesconto(self):
   #     percentual_desconto()

    def teste_percentual_desconto_deve_retornar_0_quando_input_for_0_50(self):
        """percentual_desconto(0 - 50.00) -> '0%'"""
        valor_entrada = 0 - 50.00
        valor_esperado = '0%'
        self.assertEqual(percentual_desconto(valor_entrada), valor_esperado)

main()