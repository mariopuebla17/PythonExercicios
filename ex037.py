n1 = int(input('Informe um número inteiro: '))
print('''Selecione qual será a base de conversão do número escolhido:
1 - Binário
2 - Octal
3 - Hexadecimal''')
escolha = int(input('Informa qual será a base: '))

if escolha == 1:
    print('O número {} em Binário é {}.'.format(n1, bin(n1)[2:]))
elif escolha == 2:
    print('O número {} em Octal é {}.'.format(n1, oct(n1)[2:]))
elif escolha == 3:
    print('O número {} em Hexadecimal é {}.'.format(n1, hex(n1)[2:]))
else:
    print('Opção incorreta. Escolha entre 1 a 3.')
