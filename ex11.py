alt = float(input('Qual a altura da parede? '))
lag = float(input('Me fala qual a largura da parede? '))
area = alt * lag
mtq = area ** (1/2)
lts = 2
qntlts = area / lts
print(area, mtq, lts)
print('Sua parede tem {}mts de altura, e tbm tem {}mts de lardura'.format(alt,lag))
print('A area quadrada é {}mts. e vai precisar de {}lts de tinta para pintar.'.format(area,qntlts))
