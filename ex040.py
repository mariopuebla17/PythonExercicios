n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é {}'.format(media))
if media < 5.0:
    print('REPROVADO!')
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
