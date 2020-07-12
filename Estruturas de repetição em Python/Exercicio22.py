"""
22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela,
como resultado, a correspondente média aritmética. O número de notas com que o aluno
pretenda efetuar o cálculo não será fornecido ao programa. o qual terminará quando for
introduzido um valor que não seja válido como nota de aprovação
"""
try:
    soma = 0
    for i in range(10,20+1):
        num = float(input('Insira uma nota de 0 a 10:  '))
        if (num > 0) and (num <= 10):
            soma = soma + num
        else:
            print('ERRO')
            exit()
    print(f'A média do aluno: {soma / 10}')
except ValueError:
    print('ERRO!!!!')