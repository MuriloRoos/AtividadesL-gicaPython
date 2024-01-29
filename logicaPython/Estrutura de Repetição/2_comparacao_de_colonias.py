'''
2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
'''

dias = 0

coloniaA = 4
coloniaB = 10

taxaA = 1.03    # equivalente a 3%
taxaB = 1.015   # equivalente a 1,5%

while coloniaA <= coloniaB:
    coloniaA = coloniaA * taxaA
    coloniaB = coloniaB * taxaB
    dias+=1

print(f'Levara {dias} para que a colonia A ultrapasse a coloniaB')