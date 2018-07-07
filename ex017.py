from math import hypot
a = int(input('Informe o comprimento do cateto do oposto: '))
b = int(input('Informe o comprimento do cateto adjacente: '))
h = hypot(a, b)
print('O comprimento da hipotenusa desse triângulo retângulo é de {}.'.format(h))
