#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
#Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:

#a. Soma de 2 n´umeros.
#b. Diferença entre 2 números (maior pelo menor).
#c. Produto entre 2 números.
#d. Divisão entre 2 números (o denominador não pode ser zero).

print("Escolha as opções: ")
print("a. Soma de 2 números.")
print("b. Diferença entre 2 números (maior pelo menor)")
print("c. Produto entre 2 números.")
print("d. Divisão entre 2 números (o denominador não pode ser zero)")
a = input("Qual a sua escolha: ")

if a == "a":
    print("Soma de dois números") #aqui seria o cálculo dentro da função e etc. 
elif a == "b":
    print("Diferença entre 2 números (maior pelo menor)") #aqui seria o cálculo dentro da função e etc. 
elif a == "c":
    print("Produto entre 2 números.") #aqui seria o cálculo dentro da função e etc. 
elif a == "d":
    print("Divisão entre 2 números (o denominador não pode ser zero)") #aqui seria o cálculo dentro da função e etc. 
else:
    print("Opção inválida.")

#OBS: não chamei funções por não saber as operações de escolha, porém a lógica do menu é
#ter um def em cada print abaixo de if/elif. 