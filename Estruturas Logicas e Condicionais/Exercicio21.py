"""
21. Escreva o meno de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida.

Escolha opção:
1 - Soma de 2 números.
2 - Diferença entre 2 números (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser zero).
"""
try:
    opcao = int(input('Escolha opção\n1 - Soma de 2 números.\n2 - Diferença entre 2 números (maior pelo menor).\n3 - Produto entre 2 números.\n4 - Divisão entre 2 números (o denominador não pode ser zero).\nEscolha a opção:  '))
    a = float(input('Insira o valor de A:  '))
    b = float(input('Insira o valor de B:  '))
    if opcao == 1:
        print(f'O resultado da soma de 2 números {a + b}')
    if opcao == 2:
        if a > b:
            print(f'A diferença entre 2 números (maior pelo menor): {a - b}')
        else:
            print(f'A diferença entre 2 números (maior pelo menor): {b - a}')
    if opcao == 3:
        print(f'O produto entre 2 números: {a * b}')
    if opcao == 4:
        if b == 0:
            print('Denominador não pode ser zero!!!')
        else:
            print(f'A divisão entre 2 números: {a / b}')
except ValueError:
    print('ERRO!!! a valor da opção tem que ser inteiro.')