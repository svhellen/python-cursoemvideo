#Desafio 18 aula 08:Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.


import math
a = int(input('Digite o valor do angulo:'))
s = math.sin (a)
c = math.cos (a)
t = math.tan (a)
print(f'O valor do seno é: {s}, do cosseno é:{c}, e da tangente é:{t}')

