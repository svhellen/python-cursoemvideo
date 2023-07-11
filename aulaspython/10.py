#nome = str(input('Olá, como você se chama? '))
#if nome.upper() == 'HELLEN':
#    print('Que nome bonito você tem.')
#print(f'Bom dia, {nome}!')

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2)/2
print(f'A sua media foi {m:.1f}.')
#if m >= 6.0:
#    print('Sua média foi boa. Parabéns!')
#else:
#    print('Sua média foi ruim. Estude mais!')
print('Parabens!' if m >= 6.0 else 'Estude mais!')
