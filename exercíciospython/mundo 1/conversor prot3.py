'''C
#include <stdio.h>
#include <stdlib.h>

// primeiro pedir qual conversao executar
//pedir valores
//fazer os calculos

int main()
{
    int x = 0;
    printf("--------------------------------------------------------\n");
    printf("               CONVERSOR DE NUMEROS 1.0                 \n");
    printf("--------------------------------------------------------\n");
    printf("Para converter Decimal para Binario digite: 1\n");
    printf("Para converter Binario para Decimal digite: 2\n");
    printf("Para converter Decimal para Hexadecimal digite: 3\n");
    printf("Para converter Hexadecimal para Binario digite: 4\n");
    printf("Digite 0 para sair.\n");
    scanf("%i", &x);

    if(x == 1){

    }


    return 0;
}


import hex

print(f'Para converter Decimal para Binário digite: 1')
print(f'Para converter Binário para Decimal digite: 2')
print(f'Para converter Decimal para Hexadecimal digite: 3')
print(f'Para converter Hexadecimal para Binário digite: 4')
print(f'Digite 0 para sair.')

x = int(input())
print(x)

if x == 3 :
    dec = int(input('Digite o número na base 10 (decimal): '))
    # Converte um inteiro para hexadecimal
    num_hex = hex.hex(255)  # '0xff'
'''


#Binario para decimal: multiplicar cada digito binario por 2^n correspondente,tabela 2^n
      #num_b = 1011011
#cada digito precisa ocupar uma casa pra multiplicar separadamente por 2^n onde o valor n corresponde a sua posição



#decimal para binario: ir distribuindo os numeros do maior para o menor ate formar o numero inteiro mas no sistema binario
#somar e diminuir os numeros, tabela binario, tabela 2^n



#hexa para binario: substituir cada digito hexa por 4 bits binarios equivalentes

digito = int(input('Digite um numero: '))
#posições
dez = digito // 10000000000 % 10
nove = digito // 1000000000 % 10
oito = digito // 100000000 % 10
sete = digito // 10000000 % 10
seis = digito // 1000000 % 10
cinco = digito // 100000 % 10
quatro = digito // 10000 % 10
tres = digito // 1000 % 10
dois = digito // 100 % 10
um = digito // 10 % 10
zero = digito // 1 % 10

print(f'Analisando o digito {digito}...')
print(f'posição dez dezena de bilhao: {dez}')
print(f'posição nove unidade de bilhao: {nove}')
print(f'posição oito centena de milhao: {oito}')
print(f'posição sete dezena de milhao: {sete}')
print(f'posição seis unidade de milhao: {seis}')
print(f'posição cinco centena de milhar: {cinco}')
print(f'posição quatro dezena de milhar: {quatro}')
print(f'posição tres unidade de milhar: {tres}')
print(f'posição dois centena: {dois}')
print(f'posição um dezena: {um}')
print(f'posição zero unidade: {zero}')

"""binario = [0000 = 0;
0001 = 1;
0010 = 2;
0011 = 3;
0100 = 4;
0101 = 5;
0110 = 6;
0111 = 7;
1000 = 8;
1001 = 9;
1010 = 10;
1011 = 11;
1100 = 12;
1101 = 13;
1110 = 14;
1111 = 15;]

hexa = [0 = 0000;
1 = 0001;
2 = 0010;
3 = 0011;
4 = 0100;
5 = 0101;
6 = 0110;
7 = 0111;
8 = 1000;
9 = 1001;
A = 1010;
B = 1011;
C = 1100;
D = 1101;
E = 1110;
F = 1111;]"""
