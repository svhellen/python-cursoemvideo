# 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco =float(input('Informe o preço do produto sem o desconto: '))
print(f'O preço promocional do produto é de \033[32m{preco-(preco*5)/100}')
