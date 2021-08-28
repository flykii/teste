dia = int(input('Quantos dia o carro foi alugado? '))
km = float(input('Quantos km rodou? '))
pordia = float(60.00)
kmrod = float (0.15)
pgdia = dia * pordia
pgkmrod = km * kmrod
print('O preço a pagar pelo carro é R${:.2f}'.format(pgdia+pgkmrod))
