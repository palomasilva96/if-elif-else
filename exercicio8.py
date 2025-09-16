# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
media = round((nota_1+nota_2+nota_3)/3,2 )

print(f'Média {media}')
if media >=7:
    print('Aprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
else:
    print('Reprovado')    