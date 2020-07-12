"""
58. Faça um programa que leia uma matriz de 4 linhas e 4 colunas contendo as seguintes informações
sobre alunos de uma disciplina, sendo todas as informações do tipo inteiro:

º Primeira coluna: Número de matrícula (use um inteiro)
º Segunda coluna: Média das prova
º Terceira coluna: Média dos trabalhos
º Quarta coluna: Nota final

Elabore um programa que:

(a) Leia as três primeiras informações de cada aluno
(b) Calcule a nota final como sendo a soma da média das provas e da média dos trabalhos
(c) Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe uma maior nota)
(d) Imprima a média aritmética das notas finais
"""
soma = 0
maior = 0
matricula = 0
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 4):
        matriz[i][j] = int(input(f'Linha: {j} - Coluna: {i} Insira um número:  '))


for j in range(0, 4):
    if j == 0:
        maior = matriz[1][j]
    x = matriz[1][j] + matriz[2][j]
    matriz[3][j] = x
    if matriz[3][j] > maior:
        maior = matriz[3][j]
        matricula = matriz[0][j]
    soma = soma + matriz[3][j]

print(matriz)

for i in range(0, 4):
    for j in range(0, 4):
        print(f'[{matriz[j][i]}]', end=' ')
    print()

print(f'A matricula: {matricula} teve a maior nota final: {maior}')
print(f'A média aritmetica: {soma/4}')
