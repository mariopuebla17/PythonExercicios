peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura (cm): '))
imc = peso / (altura ** 2)

print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
