#REVER


#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
#valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
#não continuar a escrever valores.

#Inicialização das variáveis
soma = 0
contador = 0
maior = float('-inf')
menor = float('inf')

while True:
    numero = int(input("Digite um número inteiro: "))
    
    #Atualiza o maior e o menor valor
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    
    soma += numero
    contador += 1
    
    opcao = input("Deseja continuar? (s/n): ")
    if opcao.lower() != 's':
        break

#Calcula a média
media = soma / contador

#Mostra os resultados
print(f"Média dos valores lidos: {media:.2f}")
print(f"Maior valor lido: {maior}")
print(f"Menor valor lido: {menor}")
