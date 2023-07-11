# 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num =float(input('Digite um numero: '))
print(f'O dobro de \033[36m{num}\033[m é:\033[32m{num*2}\033[m, seu triplo é:\033[32m{num*3}\033[m e sua raiz quadrada é:\033[31m{num**(1/2):.2f}\033[m')
