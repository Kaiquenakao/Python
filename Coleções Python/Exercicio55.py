"""
55. Faça um programa para corrigir uma prova de 10 questões de múltipla escolha (a, b, c,d ou e), em
uma turma com 3 alunos. Cada questão vale 1 ponto. Leia o gabarito, e para cada aluno leia sua
matricula (número inteiro) e suas respostas. calcule e escreva: Para cada aluno, escreva sua matricula,
suas respostas, e sua nota. O percentual de aprovação, assumindo a média 7.0.
"""

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
gabarito = ['a', 'b', 'c', 'a', 'd', 'e', 'a', 'b', 'a', 'c']
notas = []
cont = 0
matricula = []
questoes = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(0, 3):
    cont = 0
    inscricao = int(input(f'Aluno {i+1} - Insira a sua matricula:  '))
    matricula.append(inscricao)
    for j in range(0, 10):
        matriz[i][j] = input(f'Aluno {i+1} - Questão {j+1} - Insira uma resposta:  ')
        questoes[i][j] = matriz[i][j]
        if matriz[i][j] == gabarito[j]:
            cont = cont + 1
    notas.append(cont)

print(f'Gabarito: {gabarito}')

for i in range(0, 3):
    print(f'Aluno {i + 1} - Matricula: {matricula[i]} - Respostas: {questoes[i]} - Nota: {notas[i]}')



