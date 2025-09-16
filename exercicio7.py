#O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) 
# e exiba uma mensagem informando se o acesso é permitido ou negado.

horario_entrada = 8
horario_saida = 18
horario_atual = int(input('Digite a hora atual (formato de 24 horas): '))

if horario_atual >= horario_entrada and horario_atual <= horario_saida:
    print('Acesso liberado')
else:
    print('Acesso negado')