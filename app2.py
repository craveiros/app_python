import os

def percentual_desconto(valor_de_compra: float):
    if (valor_de_compra <= 75.00):
        return os.environ['DESCONTO_INTERVALO_1']
    if (valor_de_compra >= 75.01) and (valor_de_compra <= 150.00):
        return os.environ['DESCONTO_INTERVALO_2']
    if (valor_de_compra >= 150.01) and (valor_de_compra <= 300.00):
        return os.environ['DESCONTO_INTERVALO_3']
    if (valor_de_compra >= 300.01):
        return os.environ['DESCONTO_INTERVALO_4']