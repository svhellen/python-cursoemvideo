# 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

'''
Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados
e menor que a soma dos outros dois lados

Dado um triângulo cujos segmentos medem a, b e c, esse triângulo somente existirá se:

a + b < c

a + c < b

b + c < c



a = > (b % c)
b + c =

if (a + b) < c , (a + c) < b , (b + c) < c :


'''

a = int(input(f'Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da tericera reta: '))

if (a + b) < c , (a + c) < b , (b + c) < c :
    print('A junção das retas podem formar um triangulo.')
else :
    print('A junção das retas não podem formar um triangulo.')

NAO TERMINADO==================================================================
