#Desafio 4 aula 07: Escreva um programa que leia um valor em metrose o exiba convertido em centímetros e milímetros.

n = float(input('Digite sua altura em metros:'))
c = n*100
m = n*1000
print(f'Sua altura em centímetros é:{n*100} e em milímetros é:{n*1000}')