'''
8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
'''

idade = int(input('informe a idade: '))

cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while idade >= 0:
    if idade >= 0 and idade <= 25:
        cont_0_25 += 1
    elif idade >= 26 and idade <= 50:
        cont_26_50 += 1
    elif idade >= 51 and idade <= 75:
        cont_51_75 += 1
    elif idade >= 76 and idade <= 100:
        cont_76_100 += 1

    idade = int(input('informe a novamente a idade: '))

print('Distribuição de idades:')
print('[0-25]:', cont_0_25)
print('[26-50]:', cont_26_50)
print('[51-75]:', cont_51_75)
print('[76-100]:', cont_76_100)
