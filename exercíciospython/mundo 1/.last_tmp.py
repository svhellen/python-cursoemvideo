#Dissecando uma variável

n = input ('Digite algo:')
print('Tipo primitivo:', (type (n)))
print ('É um número?', (n.isnumeric()))
print('É alfabético?',(n.isalpha()))
print('É maiúsculo?', (n.isupper()))
print('É minúsculo?', (n.islower()))
print ('É alfanumérico?', (n.isalnum()))