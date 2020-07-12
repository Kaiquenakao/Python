"""
47. Faça um programa que apresente um menu de opções para o cálculo das seguintes operações
entre dois números:
"""
try:
    while True:
        opcao = int(input('Menu de opções\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n'
                          '4 - Divisão\n5- Saída\nDigite a sua opção:  '))
        if (opcao > 0) and (opcao <= 5):
            a = float(input('Insira um valor para A:  '))
            b = float(input('Insira um valor para B:  '))
            if opcao == 1:
                print(f'Você escolheu a opção Adição\nO seu resultado: {a + b}')
                break
            if opcao == 2:
                print(f'Você escolheu a opção subtração\nO seu resultado {a - b}')
                break
            if opcao == 3:
                print(f'Você escolheu a opção multiplicação\nO seu resultado {a * b}')
                break
            if opcao == 4:
                print(f'Você ecolheu a opção divisão\nO seu resultado {a / b}')
                break
            if opcao == 5:
                print('Saída\nPrograma finalizado')
                break
        else:
            print('Opção inválida\nPrograma finalizado')
            break
except ValueError:
    print('ERRO!!! Não pode ser digitado letras')