# Programa que lê três números e mostra o maior deles

# float - aceita números inteiro e decimais
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

# Verifica qual número pe maior
if n1 >= n2 and n1 >= n3:
   print(n1,"é o maior")
elif n2 >= n1 and n2 >= n3:
  print(n2, "é o maior")
else:
  print(n3, "é o maior:")
