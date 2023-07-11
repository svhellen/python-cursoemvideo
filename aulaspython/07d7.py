#Desafio 7 aula 7:Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la. Sabendo que cada litro de tinta pinta uma area de 2m². 

l = int(input('Qual a largura da parede?'))
a = int(input('Qual a altura da parede?'))
ar = l*a
lt = ar/2
print(f'Voce vai precisar de {lt} litros pra pintar {ar}m² de parede.')
 