'''
1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

'''

numero1= int(input('coloque um número: '))
numero2= int(input('coloque outro número: '))

if numero1 < numero2:
    for i in range(numero1, numero2 + 1):
        print(i)
else:
    for i in range(numero2, numero1 + 1):
        print(i)
