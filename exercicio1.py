# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
# Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

macas = int(input('Digite a quantidade de maçãs vendidas: '))
bananas = int(input('Digite a quantidade de bananas vendidas: '))

if macas > bananas:
    print("As maçãs tiveram mais vendas.")
elif bananas > macas:
    print("As bananas tiveram mais vendas.")
else:
    print("As vendas foram iguais.")