#Desafio 8 aula 07: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

#5% = 5/100   5% de 100 = 100*5/100
p1 = int(input('Preço normal do produto:'))
p2 = p1-(p1*5/100)
print(f'O preço do produto com 5% de desconto sai a {p2} reais.')


