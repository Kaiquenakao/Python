"""
24. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do
aluno e o segundo representando a sua altura em metros. Encontre o aluno mais baixo e o aluno
mais alto. Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.
"""
aluno = []
altura = []

for i in range(1, 10+1):
    n = int(input(f'{i} - Insira o número do aluno:  '))
    aluno.append(n)

for i in range(1, 10+1):
    n = float(input(f'{i} - Insira a altura em m:  '))
    altura.append(n)

alunoaltura = list(zip(aluno, altura))
print(f'Numero e altura do aluno mais alto:  {max(alunoaltura, key=lambda x: x[1])}')
print(f'Número e altura do aluno mais baixo:  {min(alunoaltura, key= lambda x: x[1])}')