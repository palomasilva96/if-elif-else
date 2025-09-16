#Escreva um programa que receba um número inteiro e exiba uma mensagem 
# informando se ele é par ou ímpar.

numero_inteiro = int(input('Digite um número inteiro: '))

if numero_inteiro % 2 == 0:
    print('número par')
else:
    print('número impar')
    