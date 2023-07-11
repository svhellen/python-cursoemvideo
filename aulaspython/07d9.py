#Desafio 9 aula 07: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s1 = int(input('Digite seu salário atual:'))
s2 = s1+(s1*15/100)
print(f'Seu salário com 15% de aumento vai para:{s2}.')