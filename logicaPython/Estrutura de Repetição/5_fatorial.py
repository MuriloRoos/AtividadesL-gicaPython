'''
5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
'''

numero = int(input('Digite um número para calcular o seu Fatorial: '))
# contador = numero
fatorial = 1
# while contador > 0:
#     print(f'{contador}', end='')
#     print(' x ' if contador > 1 else ' = ', end='')
#     fatorial = fatorial * contador
#     contador -= 1
# print(fatorial)

for i in range(numero, 0, -1):
    print(i , end='')
    print(' x ' if i > 1 else ' = ', end='')
    fatorial = fatorial * i
print(fatorial)