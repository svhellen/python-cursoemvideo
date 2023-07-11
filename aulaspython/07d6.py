#Desafio 6 aula 07:Crie um programa que leia quanto a pessoa tem na carteira e mostre quantos dolores ela pode comprar. 

n = int(input('Quanto vc tem em reais?'))
#Dolar fechado em 5 reais: 
d = n/5
print(f'Voce pode comprar {n/5}')
print(f'Voce pode comprar {d}')

#Dolar variavel
n = int (input ('Quanto vc tem em reias? '))
d = float (input ('Quanto ta o dolar hoje? '))
print (f'Com {n} reais voce pode comprar ate {n/d:.3f} dolares hoje. ')