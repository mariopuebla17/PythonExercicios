casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Informe em quantos anos você irá pagar: '))
prestacao = float(casa / (anos * 12))

print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.'.format(casa, anos, prestacao))

if prestacao > salario * 0.3:
    print('A prestação excedeu 30% do seu salário. Empréstimo NEGADO!')
else:
    print('A prestação NÃO excedeu 30% do seu salário. Empréstimo AUTORIZADO!')
