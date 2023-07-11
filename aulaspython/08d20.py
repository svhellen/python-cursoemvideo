#Desafio 20 aula 08: O mesmo professor do desafio anterior quer sortear a ondem da apresentacao de trabalhos dos alunos.Faça um programa que leia o nome dos quatro alunos e mostre a ontem dos sorteados

import random
a1 = input('Digite o nome do primeiro aluno:')
a2 = input('Digite o nome do segundo aluno:')
a3 = input('Digite o nome do terceiro aluno:')
a4 = input('Digite o nome do quarto aluno:')
alunos = [a1, a2, a3, a4]
sort = random.sample (alunos, 4)
print(f'A ondem da apresentação sera:{sort}!')