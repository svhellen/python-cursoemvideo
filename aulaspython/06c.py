#Desafio 01 aula 06: Crie um programa que leia dois numeros e mostre a soma entre eles.

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
print(f' A soma entre {n1} e {n2} é igual a {s}')

#Desafio 02 aula 06: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

#n = int(input ('Digite algo:')
#n = float(input ('Digite algo:')
#n = bool(input ('Digite algo:')
#n = str(input ('Digite algo:')
#NAO ESPECIFICADO MOSTRA STRING
n = input ('Digite algo:')
print (n.isnumeric())
print(n.isalnum())
print(n.isalpha())
print(n.isspace())
print (type(n))