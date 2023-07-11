#Desafio 2 aula 08: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa


import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
#h = (co**2+ca**2)**(0.5)
h = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é: {h:.2f}')


