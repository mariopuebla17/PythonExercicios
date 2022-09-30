from random import randint
from time import sleep

print('-=-' * 20)
print('JO-KEN-PÔ!')
print('-=-' * 20)
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !')
print('-=-' * 20)
print('''Computador jogou {}
Jogador jogou {}'''.format(itens[cpu], itens[jogador]))
print('-=-' * 20)
if cpu == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif cpu == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif cpu == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
