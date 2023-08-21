#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão.
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
a = int(input("Você deseja fazer qual tipo de conversão? "))
b = float(input("Qual temperatura você deseja converter? "))
if a == 1:
    f = b * (9 / 5) + 32
    print(b,"°C são ", f, "°F")
elif a == 2:
    c = (b - 32) * (5 / 9)
    print(b,"°F são ", c, "°C")
else:
    print("Resposta inválida.")