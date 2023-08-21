#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
#digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
#Desconsiderando o valor 1000 da parada.

contador = 0
soma = 0

#Loop para leitura dos números
while True:
    numero = int(input("Digite um número inteiro (digite 1000 para parar): "))
    
    if numero == 1000:
        break
    
    contador += 1
    soma += numero

#Mostra os resultados
print(f"Foram digitados {contador} números.")
print(f"A soma dos números digitados é: {soma}")

