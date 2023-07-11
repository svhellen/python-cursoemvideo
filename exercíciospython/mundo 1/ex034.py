# 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

si = float(input('Valor do salario atual R$: '))
if si > 1250.00:
    print(f'Seu salario atualizado será de R${si + (si * 10)/100:.2f}')
else :
    print(f'Seu salarios atualizado fica no valor de: R${si + (si *15)/100:.2f}')
