"""
13. Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a
segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e
indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos.
"""
try:
    nota1 = float(input('Insira a nota da primeira prova de 0 a 100:  '))
    nota2 = float(input('Insira a nota da segunda prova de 0 a 100:  '))
    nota3 = float(input('Insira a nota da terceira prova de 0 a 100:  '))
    media = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / 4
    if media >= 60:
        print(f'APROVADO!!!! sua nota foi {media} acima de 60 pontos')
    else:
        print(f'REPROVADO!!!! sua nota foi {media} abaixo de 60 pontos')
except ValueError:
    print('ERRO!!! só pode ser digitados números')