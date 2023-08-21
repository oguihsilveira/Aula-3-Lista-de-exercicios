#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
#As condições para aposentadoria são:
#• Ter pelo menos 65 anos,
#• Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

a = int(input("Informe a sua idade: "))
b = int(input("Informe: quantos anos você trabalhou: "))
if a >= 65 or b >= 30:
    print("Você pode se aposentar.")
elif a >= 60 and b >= 25:
    print("Você pode se aposentar.")
else:
    print("Você não pode se aposentar.")