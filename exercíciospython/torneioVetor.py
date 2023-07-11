'''
Var
   // Seção de Declarações das variáveis
   i,j: inteiro
   nome, time: vetor[1..3] de caractere
   aux: caractere
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   escreval("------------------------------")
   escreval("CAMPEONATO DE FUTEBOL")
   escreval("------------------------------")

   para i <- 1 ate 3 faca
      escreva("Digite o nome do ",i,"o. time: ")
      leia(nome[i])
   fimPara

   para i <- 1 ate 3 faca
      para j <- i + 1 ate 4 faca
         se( nome[i] = nome[j] ) entao
            j <- j + 1
            //    aux <- nome[i]
            //    nome[i] <- nome[j]
            //nome[j] <- nome[j]
            //  escrevaL(aux:12,"[ ] x [ ]     ",nome[i])
            //escrevaL(aux:12,"[ ] x [ ]            ",nome[j])
         fimSe
      fimPara
   fimPara

   para i <- 1 ate 4 faca
      escrevaL(aux:12,"[ ] x [ ]     ",nome[i])
   fimPara
'''

i = int
j = int
var = nome[3]
