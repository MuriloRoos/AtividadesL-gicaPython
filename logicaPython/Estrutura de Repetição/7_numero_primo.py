'''
7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
'''


numero = int(input('informe um numero inteiro: '))


if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f'{numero} não é um número primo')
            break
    else:
        print('é um numero primo')
else:
    print('não é um numero primo')
