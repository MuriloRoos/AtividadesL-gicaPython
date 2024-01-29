'''
4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
'''
temperatura = int(input('informe a temperatura:'))

soma = 0
contMedia = 0

while (temperatura != -273):
    soma += temperatura
    contMedia += 1

    temperatura = int(input('informe a temperatura:'))

media = soma / contMedia
print(f'A média de temperatura é de {media}°C')