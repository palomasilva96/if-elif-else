# Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

# Até 100 km: R$ 10,00
# Entre 100 km e 200 km: R$ 20,00
# Acima de 200 km: R$ 30,00
# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.


distancia_percorrida = int(input('Digite a distância percorrida (em km): '))

if distancia_percorrida <= 100:
    print('valor do pedágio é R$ 10,00')
elif distancia_percorrida >= 100 and distancia_percorrida <= 200:
    print ('Valor do pedágio é R$ 20,00')
else:
    print('Valor do pedágio é R$ 30,00')