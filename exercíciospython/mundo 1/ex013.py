#  013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario =float(input('Valor do salario atual: '))
print(f'Seu salario com reajuste de 15% vai para \033[32m{salario+(salario*15)/100}')
