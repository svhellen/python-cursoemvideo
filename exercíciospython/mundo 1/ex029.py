# 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
import time

frase = str(print('------Checagem de velocidade e calculadora de multa.------'))
h = time.strftime('%H:%M',time.localtime())
v = float(input('Velocidade do carro em km/h: '))
m = (v - 80) * 7
a = v - 80
if v > (80):
    print(f'Carro a {v}km/h. Sujeito a multa pois está {a}km acima do limite.')
    print('Calculando multa...')
    print(f'Multa de {m} reais.')
    print('Dirija com segurança!')
else :
    print(f'Carro a {v}km/h, dentro do limite de velocidade. Continue respeitando os limites.')

if h >= '5:00' and h <= '12:00':
    print(' Tenha um bom dia!')
elif h > '12:00' and h <= '17:59':
    print('Tenha uma boa tarde!')
else :
    print('Tenha uma boa noite!')

