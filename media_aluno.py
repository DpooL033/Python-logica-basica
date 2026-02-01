# Programa para calcular a média de um aluno.
# Exercício de lógica de programação em Python.

#input - pergunta o nome do aluno.
nome = input("Digite seu nome: ")

#float aceita números inteiros e decimais, pedindo e o input vai pedir a nota. 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# A media vai receber a nota1 mais a nota2 e dividir em 2 e guardar o resultado.
media = (nota1 + nota2) / 2

print("Média", media)

# o if vai verificar se a media é maior ou igual a 7.
if media >= 7:

# O print vai imprimir na tela se (Aprovado) se a media for maior ou igual a 7 
  print(nome, "Foi provado!")

# O else - se não vai imprimir (Reprovado!)
else:
  print(nome, "Reprovado!")
