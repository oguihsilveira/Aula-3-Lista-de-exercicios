#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

a = float(input("Digite a nota da primeira prova: "))
b = float(input("Digite a nota da segunda prova: "))
c = float(input("Digite a nota da terceira prova: "))
if a < 0 or a > 5 or b < 0 or b > 5 or c < 0 or c > 10:
    print("Notas devem estar entre 0 e 10")
else:
    media = (a + b + c) / 2

    if media >= 6.0:
        print(f"Média: {media:.2f}")
        print("Status: Aprovado")
    else:
        print(f"Média: {media:.2f}")
        print("Status: Reprovado")