# Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

# O valor da renda mensal precisa ser maior que R$ 2.000,00.
# O valor da parcela não pode ultrapassar 30% da renda.
# Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada.
# O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

renda_mensal = float(input('Digite o valor da sua renda mensal: '))
parcela_desejada  = float(input('Digite o valor da parcela desejada: '))
limite = renda_mensal * 0.30



if renda_mensal <= 2000:
    print('empréstimo negado: valor menor que R$ 2.000,00')
elif parcela_desejada > limite:
    print('empréstimo negado: parcela acima de 30%')
else:
    print('Empréstimo solicitado com sucesso')
