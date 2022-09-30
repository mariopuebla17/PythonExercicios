from datetime import date

anoNasc = int(input('Informe seu ano de nascimento: '))
anoAtual = date.today().year

if anoAtual - anoNasc < 18:
    print('Ainda faltam {} anos para seu alistamento!'.format(18 - (anoAtual - anoNasc)))
elif anoAtual - anoNasc == 18:
    print('Você está no ano de alistamento!')
else:
    print('Você passou da idade de alistamento. Deveria ter se alistado há {} anos.'.format((anoAtual - anoNasc) - 18))
