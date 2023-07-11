# 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = int(input('Distância da viagem em km: '))
x  = km * 0.50 if km <= 200 else km * 0.45
if km <= 200:
    print(f'O valor da passagem será de {km * 0.50:.2f} reais.')
else :
    print(f'O valor da viagem será de {km * 0.45:.2f} reais.')
print(f'Sua viagem de {km}km custará R${x:.2f}.')
