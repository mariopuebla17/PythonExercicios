from datetime import date

anoNasc = int(input('Informe seu ano de nascimento: '))

if date.today().year - anoNasc <= 9:
   print('Sua categoria é: MIRIM')
elif 10 <= date.today().year - anoNasc <= 14:
   print('Sua categoria é: INFANTIL')
elif 15 <= date.today().year - anoNasc <= 19:
   print('Sua categoria é: JÚNIOR')
elif 20 <= date.today().year - anoNasc <= 25:
   print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER')
