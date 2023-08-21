#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
#trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
#ao final mostrar seu nome e salário final calculado.
a = input("Digite seu nome: ")
b = int(input("Quantas horas são trabalhadas por dia: "))
c = float(input("Quanto você recebe por hora trabalhada: "))
print(f"Seu salário bruto é R${b*c}")
print(f"Seu salário com desconto de 2% é R${(b*c) *0.98}")