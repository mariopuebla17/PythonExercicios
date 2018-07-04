preco = float(input('Informe o valor original do produto: R$'))
desc = preco * 0.05
precoFinal = preco - desc
print('O valor desse item com 5% de desconto é R$ {:.2f} reais.'.format(precoFinal))
