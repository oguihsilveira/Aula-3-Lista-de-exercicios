#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
#tela dizendo se está “quente”, “frio” ou “agradável”.
a = float(input("Qual a temperatura atual? "))
if a <= 18.00 and a >= -10.00:
    print(a, "°C é uma temperatura fria.")
elif a >= 19.00 and a <= 23.00:
    print(a, "°C é uma temperatura agradável.")
elif a >= 24.00 and a <= 40.00:
    print(a, "°C é uma temperatura quente.")
else:
    print(a, "°C é uma temperatura muito difícil de se sobreviver... 💀")