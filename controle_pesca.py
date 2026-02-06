
# Controle de Pesca - Cálculo de Multa
Este projeto em Python simula o controle de pesca,
verificando se o peso de peixes pescado ultrapassou 
o limite permitido calculando a multa quando necessário.

## Descrição do problema
De acordo com a legislação:
- O limite permitido é **50 kg de peixes**
- Para cada quilo excedente, é aplicada uma multa de **R$ 4,00**

O programa:
- Solicita o peso total de peixes pescados
- Verifica se houve excesso
- Calcula o valor da multa, aplicável
- Exibe mensagens claras para o usuário

## Conceitos praticados
- Entrada de daos ('input')
- Conversão de tipos ('float')
- Estruturas condicionais ('if / else')
- Operações matemáticas
- Uso de f-strings
- Boas praticas de legibilidade

## Codigo principal

peso = float(input("Digite o peso de peixe: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"João pescou {peso}Kg de peixe")
    print(f"E ultrapassou {excesso}kg a mais do permitido ")
    print(f"O valor da multa é R${multa}")
else:
    print(f"João pescou {peso}Kg de peixe")
    print("Não houve excesso. Multa R$0.00")
