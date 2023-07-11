# 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero:'))
c = int(input('Digite outro numero: '))

#ab
if a > (b & c) and b < c:
    print(f'O numero {a} é o maior. ')
    print(f'E o menor é {b}')
elif b > (a & c):
    print(f'O numero {b} é o maior.')
else :
    print(c)


