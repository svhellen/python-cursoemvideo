# Dissecando uma variável
# 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.



'''
n = input ('Digite algo: ')
print(f'Tipo primitivo: {type (n)}')
print(f'É um número? ', (n.isnumeric()))
print(f'É alfabético? ',(n.isalpha()))
print(f'Está tudo maiúsculo? ', (n.isupper()))
print(f'Está tudo minúsculo? ', (n.islower()))
print(f'É alfanumérico? ', (n.isalnum()))
print(f'Só tem espaços? ', (n.isspace()))
print(f'Está capitalizada? {n.istitle()}')
'''
cores = {'limpa' : '\033[m',
         'verde' : '\033[32m',
         'vermelho' : '\033[31m'}

n = input ('Digite algo: ')
#y = print('\033[32m Sim.\033[m' if x == True else '\033[31m Não. \033[m')

print(f'Tipo primitivo: (type (n))')
print(f'É um número? ' \033[32m Sim.\033[m' if (n.isnumeric()) == True else '\033[31m Não. \033[m)
print(f'É alfabético? ' '\033[32m Sim.\033[m' if (n.isalpha()) == True else '\033[31m Não. \033[m')
print(f'Está tudo maiúsculo? ' '\033[32m Sim.\033[m' if (n.isupper()) == True else '\033[31m Não. \033[m')
print(f'Está tudo minúsculo? ' '\033[32m Sim.\033[m' if (n.islower()) == True else '\033[31m Não. \033[m')
print(f'É alfanumérico? ' '\033[32m Sim.\033[m' if (n.isalnum()) == True else '\033[31m Não. \033[m')
print(f'Só tem espaços? ' '\033[32m Sim.\033[m' if (n.isspace()) == True else '\033[31m Não. \033[m')
print(f'Está capitalizada? ' '\033[32m Sim.\033[m' if (n.istitle()) == True else '\033[31m Não. \033[m')

