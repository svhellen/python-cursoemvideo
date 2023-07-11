# Dissecando uma variável
# 004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.




n = input ('Digite algo:')
print('Tipo primitivo:', (type (n)))
print('É um número?', (n.isnumeric()))
print('É alfabético?',(n.isalpha()))
print('É maiúsculo?', (n.isupper()))
print('É minúsculo?', (n.islower()))
print('É alfanumérico?', (n.isalnum()))
