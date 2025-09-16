#Calcular IMC

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/altura**2

print(f'seu IMC é {imc}')

if imc<18.5:
    print('Você está abaixo do peso')
elif imc>=18.5 and imc<=25:
    print('você está no peso ideal')
else:
    print('Acima do peso')