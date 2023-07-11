'''
Var
   // Seção de Declarações das variáveis
   alunos,x:inteiro
   nome:caractere
   notaAtu,notaAnt:real
   melhorAluno:lista
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   x <- 1
   notaAnt <- 0

   escrevaL("----------------------------")
   escrevaL("   Escola Santa Paciencia   ")
   escrevaL("----------------------------")
   escreva("Quantos alunos a turma tem? ")
   leia(alunos)
   enquanto (x <= alunos) faca
      escrevaL("ALUNO ",x)
      escreva("Nome do aluno: ")
      leia(nome)
      escreva("Nota de ",nome)
      leia(notaAtu)
         se (notaAtu > notaAnt) entao
             melhorAluno <- (notaAtu , nome , x):lista
         fimSe
      notaAnt <- notaAtu
      x <- x + 1
      fimEnquanto
      escreva(melhorAluno)
'''
x = 1
notaAnt = 0
alunos = int(input('Quantos alunos a turma tem? '))
melhorAluno = []
melhorAluno2 = []
while (x <= alunos):
    print('ALUNO ',x)
    nome = input('Nome do aluno: ')
    notaAtu = float(input('Nota de '+nome+': '))
    if (notaAtu > notaAnt):
        melhorAluno = [nome,notaAtu,x]
    #elif (notaAtu == notaAnt):
    #        melhorAluno2 =

    notaAnt = notaAtu
    x = x + 1
print(f'A maior nota foi do {melhorAluno[x]}, {melhorAluno[nome]} com nota {melhorAluno[notaAtu]} .')
