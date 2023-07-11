# 002 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boasvindas para ela:
# Ex:
# Qual é o seu nome? João da Silva
# Olá João da Silva, é um prazer te conhecer!


nome = input("oie, como vc se chama?")
print("Bem vindo(a)", nome)

nome = input("Digite seu nome:")
print("Prazer em conhecer você, {}".format(nome))

nome = input("Digite seu nome:")
print(f"Oie {nome}, seja bem vindo!")
