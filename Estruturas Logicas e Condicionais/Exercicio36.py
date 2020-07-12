"""
36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
-------------------------------------------------------------------------------------------
|                        Venda mensal                       |     Comissão                |
| Maior ou igual a R$ 100.000,00                            | R$ 700,00 + 16% das vendas  |
| Menor que R$ 100.000,00 e maior ou igual a R$ 80.000,00   | R$ 650,00 + 14% das vendas  |
| Menor que R$ 80.000,00 e maior ou igual a R$ 60.000,00    | R$ 600,00 + 14% das vendas  |
| Menor que R$ 60.000,00 e maior ou igual a R$ 40.000,00    | R$ 550,00 + 14% das vendas  |
| Menor que R$ 40.000,00 e maior ou igual a R$ 20.000,00    | R$ 500,00 + 14% das vendas  |
| Menor que R$ 20.000,00                                    | R$ 400,00 + 14% das vendas  |
"""
try:
    venda = float(input('Insira o valor da venda:  '))
    if venda > 0:
        if venda >= 100000:
            print(f'O valor da sua venda é {venda} - a sua comissão é {round(((venda * 0.16) + 700),2 )} reais')
        if (venda < 100000) and (venda >= 80000):
            print(f'O valor da sua venda é {venda} - a sua comissão é {round(((venda * 0.14) + 650),2 )} reais')
        if (venda < 80000) and (venda >= 60000):
            print(f'O valor da sua venda é {venda} - a sua comissão é {round(((venda * 0.14) + 600), 2)} reais')
        if (venda < 60000) and (venda >= 40000):
            print(f'O valor da sua venda é {venda} - a sua comissão é {round(((venda * 0.14) + 550), 2)} reais')
        if (venda < 40000) and (venda >= 20000):
            print(f'O valor da sua venda é {venda} - a sua comissão é {round(((venda * 0.14) + 500), 2)} reais')
        if venda < 20000:
            print(f'O valor da sua venda é {venda} - a sua comissão é {round(((venda * 0.14) + 400), 2)} reais')


    else:
        print('Valor inválido!!!')

except ValueError:
    print('ERRO!!!! Só pode ser digitado números ')