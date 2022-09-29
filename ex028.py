from random import randint

print('===== VOU PENSAR EM UM NÚMERO ENTRE 0 E 5. DESCUBRA!=====')
n1 = int(input('Digite um número: '))
n2 = randint(0, 5)
if n1 == n2:
    print('Você digitou {}, e a máquina sorteou o número {}. \nACERTOU!'.format(n1, n2))
else:
    print('Você digitou {}, e a máquina sorteou o número {}. \nERRRRRRRROU!'.format(n1, n2))
