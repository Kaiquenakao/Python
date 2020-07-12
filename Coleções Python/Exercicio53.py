"""
53. Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo.
Sabendo que cada cartela devera conter 5 linhas de 5 números, gere estes dados de modo a não ter
números repetidos dentro das cartelas. O programa deve exibir na tela a cartela gerada.
"""
import random

cont = 0


vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []

cartela = [vetor1, vetor2, vetor3, vetor4, vetor5]

# vetor1
while cont < 5:
    x = random.randint(1, 99)
    if x not in vetor1:
        vetor1.append(x)
        cont = cont + 1

# vetor2
cont = 0
while cont < 5:
    x = random.randint(1, 99)
    if x not in vetor2:
        vetor2.append(x)
        cont = cont + 1

# vetor3
cont = 0
while cont < 5:
    x = random.randint(1, 99)
    if x not in vetor3:
        vetor3.append(x)
        cont = cont + 1

# vetor4
cont = 0
while cont < 5:
    x = random.randint(1, 99)
    if x not in vetor4:
        vetor4.append(x)
        cont = cont + 1

# vetor5
cont = 0
while cont < 5:
    x = random.randint(1, 99)
    if x not in vetor5:
        vetor5.append(x)
        cont = cont + 1

for i in range(0, 5):
    for j in range(0, 5):
        print(f'[{cartela[i][j]}]', end=' ')
    print()
