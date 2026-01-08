while True:
  maior_altura = -1
  indice_maior = 0

for i in range(8):
  altura = int(input())
  if altura > maior_altura:
    maior_altura = altura
    indice_maior = i
print(indice_maior)    
