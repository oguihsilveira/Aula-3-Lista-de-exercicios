#Aluno: Guilherme Henrique Machado Silveira
#Professora: Mariane Melo
#Turma: 2137

#Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
#quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
a = float(input("Digite a altura da parede: "))
b = float(input("Digite a largura da parede: "))
c = a * b #área
d = c / 2
print("Para pintar ", c, "m2 de parede, você precisa de: ", d, "L de tinta")