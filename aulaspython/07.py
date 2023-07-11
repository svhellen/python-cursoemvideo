# Operadores aritméticos

# + = adição
# - = subtração
# * = multiplicação
# / = divisão
# ** = potência
# // = divisão inteira (divisão q nao usa vírgula)
# % = módulo/resto da divisão 

# operando/operadores/operando/igual

# 5+2==7
# 5-2==3
# 5*2==10
# 5/2==2.5
# 5**2==25
# 5//2==2
# 5%2==1

# Ordem de precedência
# 1 = ()
# 2 = **
# 3 = *, /, //, %
# 4 = +, -

# 5+3*2==11
# 3*5+4**2==16+3*5==16+15==31
# 3*(5+4)**2==3*9**2==3*81==243

# Raiz quadrada de um número é igual a eleva-lo a potência de meio
# 81**(1/2) == 9.0 raiz quadrada de 81
# 25**(1/2) == 5.0 raiz quadrada de 25
# Raiz cúbica = número elevado a (1/3)
# 127**(1/3)

#######
# 'oi'*5
# oioioioioi
# '+'*3
# +++
# print ('oi'*3)
# oioioi


nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer, {nome}!')
print(f'Prazer em te conhecer, {nome:20}!')
print(f'Prazer em te conhecer, {nome:>20}!')
print(f'Prazer em te conhecer, {nome:<20}!')
print(f'Prazer em te conhecer, {nome:^20}!')
print(f'Prazer em te conhecer, {nome:#^20}!')

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma dos valores {n1} e {n2} resulta em:{n1 + n2}!')
print(f'A subtração dos valores {n1} e {n2} resulta em:{sub}!')
print(f'A multiplicação dos valores {n1} e {n2} resulta em:{m}!')
print(f'A divisão entre os valores {n1} e {n2} resulta em:{d}!')
print(f'A divisão inteira dos valores {n1} e {n2} resulta em:{di}!')
print(f'{n1} elevado a {n2} é {e}!')
print(f'A soma é {s}, a divisão é {d} e a multiplicação é {m}')
#:.3f = três casas decimais flutuantes
print(f'A divisão é {d:.3f}!')
# pra quebrar a linha \n
print(f'A soma é {s} \n a divisão é {d} \n e a multiplicação é {m}')
# pra nao quebrar a linha ,end=''
print(f'A soma é {s}', end='>>>')
print(f'A divisão é {d}', end='!!!')
