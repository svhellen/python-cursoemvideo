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
'''

#import hex

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
    # num_hex = hex.hex(255)  # '0xff'

