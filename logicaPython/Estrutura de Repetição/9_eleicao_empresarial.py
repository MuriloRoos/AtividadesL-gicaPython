'''
9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).

Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
'''

joaodaSilva_1 = 0
camilaOliveira_2 = 0
pedroSantos_3 = 0
larissaCosta_4 = 0
votosNulos_5 = 0
votosBrancos_6 = 0


for i in range(20):
    voto = int(input('vote aqui: '))
    if (voto == 1):
        joaodaSilva_1 += 1
    elif (voto == 2):
        camilaOliveira_2 += 1
    elif (voto == 3):
        pedroSantos_3 += 1
    elif (voto == 4):
        larissaCosta_4 += 1
    elif (voto == 5):
        votosNulos_5 += 1
    elif (voto == 6):
        votosBrancos_6 += 1
    else:
        print("Voto inválido.")

total_votos = joaodaSilva_1+camilaOliveira_2+pedroSantos_3+larissaCosta_4+votosNulos_5+votosBrancos_6

porcentagemNulos = (votosNulos_5 / total_votos) * 100
porcentagemBrancos = (votosBrancos_6 / total_votos) * 100

print("João da Silva:", joaodaSilva_1)
print("Camila Oliveira:", camilaOliveira_2)
print("Pedro Santos:", pedroSantos_3)
print("Larissa Costa:", larissaCosta_4)
print("Votos Nulos:", votosNulos_5)
print("Votos Brancos:", votosBrancos_6)
print(f'porcentagem de votos nulos em relação ao total de votos: {porcentagemNulos}')
print(f'porcentagem de votos em branco em relação ao total de votos: {porcentagemBrancos}')