# 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome completo em letras maiusculas: ',(nome.upper()))
print(f'Seu nome completo em letras minusculas: ',(nome.lower()))
#print(f'Seu nome completo tem ',(len(nome.replace(' ',''))),' letras.')
print(f'Seu nome completo tem ',(len(nome) - nome.count(' ')))
#print(f'Seu primeiro nome tem ',(nome.find(' ')),' letras.')
dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]} e tem {len(dividido[0])} letras.')
