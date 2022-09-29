print('-=-' * 20)
print('PAR OU ÍMPAR?')
print('-=-' * 20)
numero = int(input('Digite um número: '))
resto = numero % 2

if resto == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('O número {} é ÍMPAR!'.format(numero))
