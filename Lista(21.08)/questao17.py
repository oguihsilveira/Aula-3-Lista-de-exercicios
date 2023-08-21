#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
#utilizando as seguintes formulas (onde h corresponde à altura):
#• Homens: (72.7 ∗ h) − 58
#• Mulheres: (62, 1 ∗ h) − 44, 7

a = input("Qual é o seu sexo? Masculino(M) & Feminino(F): ")
b = float(input("Informe sua altura: "))
if a == "M":
    c = (b * 72.7) - 58
    print(f"Seu peso ideal é {c}")
elif a == "F":
    c = (b * 62.1) - 44, 7
    print(f"Seu peso ideal é {c}")
else:
    print("O sexo é inválido.")