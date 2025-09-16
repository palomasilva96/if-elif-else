# Estabelecer um limite mensal de R$ 3.000,00  com um programa que ajude a controlar suas despesas

limite = 3000
despesas_do_mes = float(input('Digite o total de despesas do mês: '))
if despesas_do_mes > limite:
    print('Atenção! Você ultrapassou o limite do orçamento')
else:
    print('Está dentro do orçamento')