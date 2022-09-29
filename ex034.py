salario = float(input('Qual é o seu salário atual? '))
if salario > 1250.00:
    print('Seu novo salário será de R${:.2f}'.format(salario + salario * 0.1))
else:
    print('Seu novo salário será de R${:.2f}'.format(salario + salario * 0.15))
