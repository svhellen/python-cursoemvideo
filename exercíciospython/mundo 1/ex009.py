# 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

'''
num =int(input('Digite um numero: '))
print(f'{num} x 1 = {num*1}')
print(f'{num} x 2 = {num*2}')
print(f'{num} x 3 = {num*3}')
print(f'{num} x 4 = {num*4}')
print(f'{num} x 5 = {num*5}')
print(f'{num} x 6 = {num*6}')
print(f'{num} x 7 = {num*7}')
print(f'{num} x 8 = {num*8}')
print(f'{num} x 9 = {num*9}')
print(f'{num} x 10 = {num*10}')
'''

x = 1
num =int(input('Digite um numero: '))
while x <= 10:
    print(f'{num}  x ', x ,f' = \033[32m{num * x}\033[m\n')
    x = x + 1

