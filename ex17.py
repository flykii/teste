import math
catop = float(input('Cateto oposto: '))
catad = float(input('Cateto Adjacente: '))
resp1 = catop**2 + catad**2
hip = math.sqrt(resp1)
print('Cateto oposto é: {} \nCateto adjacente é: {} \nA hipotenusa é: {:.2f} '.format(catop,catad,hip))