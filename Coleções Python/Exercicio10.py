"""
10. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor calcule
e imprima a média geral
"""
import statistics
notas = []
for i in range(1,5):
    nota = float(input(f'Aluno{i}:Insira a sua nota:'))
    if nota < 10 and nota > 0:
        notas.append(nota)
print(f'Média geral: {statistics.mean(notas)}')