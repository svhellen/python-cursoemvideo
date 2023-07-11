# frase = ('Curso em vídeo python')
# print frase[5] -> ele vai printar o 5 caráctere (ultimo valor desconsiderado)
# print frase [2:5] -> ele vai printar do caráctere 2 ao 5
# print frase [:5] -> vai printar do início até o caráctere 5
# e se não sabe onde termina, pode definir onde começa
# print frase [9::3] -> vai printar do 9 até o fim, e pular 3

# len(frase) -> analisa o comprimento da string
# frase.count('o') -> manda contar quantas vezes aparece a letra 'o'
# frase.count('o',0,13) -> fatiamento dentro do count, quantas vezes
      # aparece 'o' do 0 ao 13.
# frase.find('deo') -> manda encontrar onde começa isso
# 'curso' in frase -> acha a string na frase
# frase.replace('python','android' -> troca a frase da string por outra
# frase.upper() -> transforma caractere em maíusculo
# frase.lower() -> faz o contrário
# frase.capitalize() -> apenas a primeira letra em maiúsculo
# frase.title() -> contabiliza quantas palavras e capitaliza todas
# frase.strip() -> remove todos os espaços inúteis de uma string
# frase.rstrip() -> remove somente os últimos espaços (da esquerda pra direita)
# frase.lstrip()-> remove os espaços da esquerda da string
# frase.split() -> faz uma divisão considerando os espaços e as transforma em lista
# '-'.join(frase) -> junta todos os elementos de frase entre a string '-'
                        # ex: curso-em-vídeo





frase = 'Curso em video Python'
print(len(frase))


