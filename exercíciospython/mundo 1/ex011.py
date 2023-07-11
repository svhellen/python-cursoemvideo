# 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar =float(input('Qual é a largura da parede? '))
alt =float(input('Qual a altura da parede? '))
print(f'\033[1mVocê vai precisar de\033[m \033[7m{(lar * alt)/2}\033[m \033[1mlitros de tinta pra pintar\033[m \033[7m{lar*alt}m2\033[m \033[1mde parede.')
