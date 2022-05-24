valor = float(input('Valor de Compra: R$ '))
perc_desc = float(input('Percentual de desconto: R$ '))

valor_desc = valor * perc_desc / 100

print('Você economizou: R$ ' + str(valor_desc))
print('Você deverá pagar: R$ ' + str(valor-valor_desc))