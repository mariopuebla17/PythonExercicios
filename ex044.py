print('-=-' * 20)
print('CAIXA')
print('-=-' * 20)
valor = float(input('Informe o valor do produto: R$ '))
print('=' * 20)
print('Selecione a forma de pagamento:')
print('''   
[1] – à vista dinheiro: 10% de desconto
[2] - à vista no cartão: 5% de desconto
[3] – em até 2x no cartão: preço formal 
[4] - 3x ou mais no cartão: 20% de juros
''')
opcao = int(input('Informe sua escolha: '))

if opcao == 1:
    print('À vista no dinheiro. Valor final: R$ {:.2f}'.format(valor - (valor * 0.1)))
elif opcao == 2:
    print('À vista no cartão. Valor final: R$ {:.2f}'. format((valor - (valor * 0.05))))
elif opcao == 3:
    print('Em até 2x no cartão. Valor final: R$ {:.2f}'.format(valor))
elif opcao == 4:
    print('Em 3x ou mais no cartão. Valor final: R$ {:.2f}'.format(valor + (valor * 0.2)))
else:
    print('Opção inválida. Tente novamente.')
