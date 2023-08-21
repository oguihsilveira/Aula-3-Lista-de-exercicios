#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Crie um programa que leia dois valores e mostre na tela um menu :
#a. Somar
#b. Multiplicar
#c. Maior
#d. Menor
#e. Sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

print("Escolha as opções: ")
print("a. Somar")
print("b. Multiplicar")
print("c. Maior")
print("d. Menor")
print("e. Sair do programa")
a = input("Qual a sua escolha: ")
if a == "a":
    print("Somar.") #aqui seria o cálculo dentro da função e etc. 
elif a == "b":
    print("Multiplicar.") #aqui seria o cálculo dentro da função e etc. 
elif a == "c":
    print("Maior.") #aqui seria o cálculo dentro da função e etc. 
elif a == "d":
    print("Menor.") #aqui seria o cálculo dentro da função e etc. 
elif a == "e":
    print("Sair do programa.") #aqui seria a saída do programa em menu. 
else:
    print("Opção inválida.")

#OBS: não chamei funções, porém a lógica do menu é
#ter um def em cada print abaixo de if/elif. 