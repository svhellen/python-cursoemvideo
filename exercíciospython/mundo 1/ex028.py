# 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''
import random
input numero 0 - 6
is 'numero' in ?????????
'''
import emoji
import random
print('DESCUBRA O NUMERO MISTERIOSO')
print('Eu vou pensar em um numero aleatório entre 0 e 5, seu trabalho é descobrir qual será')

nc = random.randint(0,5)
print(str('Pensando...'))
print('Pronto!')
print(nc)
nu = int(input('Qual é o seu palpite?'))
if nc == nu :
    print('MEU DEUS, C-COMO VOCÊ ADVINHOU?? ', emoji.emojize(':flushed:',language="alias"))
    print('Parabêns... usuario de bola de cristal.', emoji.emojize(':face_with_raised_eyebrow:', language='alias'))
else :
    print(f'He he, não foi dessa vez. {emoji.emojize(":pensive:", language= "alias")}')

