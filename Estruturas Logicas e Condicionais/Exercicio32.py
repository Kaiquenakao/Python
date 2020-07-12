"""
32. Escrever um programa que leia o código do produto escolhido do cardápio de uma
lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete
segue o padrão abaixo:
-----------------------------------------------------------------
|       Especificação        |     Código            |  PREÇO    |
|     Cachorro quente        |        100            |   1.20    |
|     Bauru simples          |        101            |   1.30    |
|     Bauru com ovo          |        102            |   1.50    |
|     Hamburguer             |        103            |   1.20    |
|     Cheeseburguer          |        104            |   1.70    |
|     Suco                   |        105            |   2.20    |
|     Refrigerante           |        106            |   1.00    |
"""
try:
    codigo = int(input('Insira o código:  '))
    if (codigo >= 100) and (codigo <= 106):
        qnt = int(input('Insira a quantidade:  '))
        if codigo == 100:
            print(f'Você escolheu cachorro quente - Preço 1.20 reais\n'
                  f'Portanto, o preço final vai ser {round(qnt * 1.20, 2)} reais')
        if codigo == 101:
            print(f'Você escolheu bauru simples - Preço 1.30 reais\n'
                  f'Portanto, o preço final vai ser {round(qnt * 1.30, 2)} reais')
        if codigo == 102:
            print(f'Você escolheu bauru com ovo - Preço 1.50 reais\n'
                    f'Portanto, o preço final vai ser {round(qnt * 1.50, 2)} reais')
        if codigo == 103:
            print(f'Você escolheu hamburguer - Preço 1.20 reais\n'
                  f'Portanto, o preço final vai ser {round(qnt * 1.20, 2)} reais')
        if codigo == 104:
            print(f'Você escolheu cheeseburguer - Preço 1.70 reais\n'
                  f'Portanto, o preço final vai ser {round(qnt * 1.70, 2)} reais')
        if codigo == 105:
            print(f'Você escolheu suco - Preço 2.20 reais\n'
                  f'Portanto, o preço final vai ser {round(qnt * 2.20, 2)} reais')
        if codigo == 106:
            print(f'Você escolheu refrigerante - Preço 1.00 reais\n'
                  f'Portanto, o preço final vai ser {round(qnt * 1.00, 2)} reais')
    else:
        print('Código inserido inválido')
        exit()
except ValueError:
    print('ERRO!!! Só pode ser digitado número inteiro')