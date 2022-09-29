print('CUSTO DA VIAGEM')
distancia = float(input(('Informe a distância da sua viagem, em Km: ')))
if distancia <= 200:
    print('O preço da sua viagem é de R${:.2f}'.format(distancia * 0.50))
else:
    print('O preço da sua viagem é de R${:.2f}'.format(distancia * 0.45))
