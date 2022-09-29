print('-=-' * 20)
print('RADAR ELETRÔNICO \nLIMITE DE VELOCIDADE: 80KM/H')
print('-=-' * 20)
velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80:
    print('MULTADO! \nVocê excedeu o limite de velocidade em {} km/h'.format(velocidade - 80))
    print('Sua multa é no valor de R${:.2f}'.format((velocidade - 80) * 7))
print('Se beber não dirija!')
