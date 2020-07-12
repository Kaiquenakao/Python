"""
35. Faça um programa que some os número ímpares contidos em um intervalo definido
pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo
e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o usuário
digite um intervalo inválido (començando por um valor maior que o valor final) deve
ser escrito uma mensagem de erro na tela, "intervalo de valores inválido" e o programa
termina. Exemplo de tela de saída: Digite o valor inicial e o valor final: 5 10
soma dos ímpares neste intervalo: 21
"""
try:
    soma = 0
    inicial = int(input('Insira o valor inicial do intervalo:  '))
    final = int(input('Insira o valor final do intervalo:  '))
    if inicial < final:
        for i in range(inicial, final + 1):
            if i % 2 == 1:
                soma = soma + i
    else:
        print('intervalo de valores inválido')
    print(f'soma dos ímpares neste intervalo: {soma}')
except ValueError:
    print('ERRO!!!')