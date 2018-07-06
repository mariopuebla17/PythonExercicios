d = int(input('Informe a quantidade de dias pelos quais o carro foi alugado: '))
km = float(input('Informe a quantidade de kilômetros percorridos: '))
p = (d * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(p))
