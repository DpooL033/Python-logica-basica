#cadastro simples de produtos em Python
Este projeto é um exercício de lógica de programação em Python.

## Funcionalidades
- Cadastro de produtos (nome e preço)
- Soma do valor total dos produtos
- Contagem de produtos com preço acima de R$100

## Conceitos utilizados 
- Entrada e saída de dados
- Estrutura de repetição(for)
- Estrutura condicional (if)
- Contador e acumulador

## Objetivo
Praticar lógica de programação e registrar a evolução nos estudos em Python.

-------------------------------------------------------------

quantidade = int(input("Quantos produtos deseja cadastrar? "))

total = 0 
produtos_mais_100 = 0

for i in range(quantidade):
    nome = input("Nome do produto: ")
    preco = float(input("preço do produto: "))

    total += preco

    if preco > 100:
      produtos_mais_100 += 1

print("\nResumo da compra")
print("Total gasto: R$", total)
print("Produtos acima de R$100:", produtos_mais_100)
