"""
14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 até 10. respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um
exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho
de Laboratório: 2; Avaliação semestral: 3; Exame final: 5. De acordo com o resultado, mostre
na tela se o aluno está reprovado (média entre 0 a 2,9), de recuperação (entre 3 a 4,9)
ou se foi aprovado. Faça todas as verificações necessárias.
"""
try:
    num = ['Trabalho de laboratório', 'Avaliação semestral', 'Exame final']
    soma = 0
    pesos = [2, 3, 5]
    for i in range(3):
        nota = float(input(f'Insira a nota do(a) {num[i]}:  '))
        if (nota >= 0) and (nota <= 10):
            soma += nota * pesos[i]
        else:
            print('ERRO!!! Sua nota foi menor que 0 e maior que 10')
            exit()
    media = soma / 10
    if (media >= 0) and (media <= 2.9):
        print(f'REPROVADO (media entre 0 a 2.9) !!! sua nota foi {media}')
    elif (media >= 3) and (media <= 4.9):
        print(f'RECUPERAÇÃO (media entre 3 a 4.9) !!! sua nota foi {media}')
    else:
        print(f'APROVADO!!! sua nota foi {media}')
except ValueError:
    print('ERRO!!')