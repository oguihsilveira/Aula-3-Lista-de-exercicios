#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
#mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
#Euros.
a = input("Digite seu nome: ")
b = float(input("Digite quantos reais você tem: "))
print(f"Seu dinheiro, convertido em dólares é: {b/4.99}")
print(f"Seu dinheiro, convertido em euros é: {b/5.41}")