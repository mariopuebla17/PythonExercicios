print('-=-' * 20)
print('RADAR ELETRÔNICO \nLIMITE DE VELOCIDADE: 80KM/H')
print('-=-' * 20)
velocidade = int(input('Informe a velocidade do carro: '))
limite = 80
if velocidade <= limite:
    print('Você está dentro da velocidade permitida!')
else:
    print('MULTADO! \nVocê excedeu o limite de velocidade em {} km/h'.format(velocidade - limite))
    print('Sua multa é no valor de R${}'.format((velocidade - limite) * 7))
