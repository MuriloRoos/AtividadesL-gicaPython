'''
6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
'''

numero = int(input('Informe um numero inteiro de 1 a 10: '))

print(f'Tabuada do {numero}:')

if (numero > 1) and (numero <= 10):
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
else:
    print('numero invalido')