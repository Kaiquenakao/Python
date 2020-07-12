"""
39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários
com menor salário terão um aumento proporcionalmente maior do que os funcionários com
um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber
um bônus adicional de salário. Faça um programa que leia:

    ° O valor do salário atual do funcionário;
    ° O tempo de serviço desse funcionário na empresa (números de anos de trabalho na empresa)

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor
do salário final reajustado, ou uma mensagem caso funcionário não tenha direito a nenhum
aumento.
--------------------------------------------------------------------------------------
| Salário atual      | Reajuste (%) | Tempo de serviço | Bônus     |
| Até 500,00         |     25%      | Abaixo de 1 ano  | Sem bônus |
| Até 1000,00        |     20%      | De 1 a 3 anos    | 100,00    |
| Até 1500,00        |     15%      | De 4 a 6 anos    | 200,00    |
| Até 2000,00        |     10%      | De 7 a 10 anos   | 300,00    |
| Acima de 2000,00   |  Sem reajute | Mais de 10 anos  | 500,00    |
"""
try:
    salatual = float(input('Insira o salário atual:  '))
    tempo = float(input('Insira o tempo de serviço (número de anos de trabalho na empresa):  '))
    if salatual > 0:
        if salatual <= 2000:
            if salatual <= 2000:
                novo = salatual * 1.10
            if salatual <= 1500:
                novo = salatual * 1.15
            if salatual <= 1000:
                novo = salatual * 1.20
            if salatual <= 500:
                novo = salatual * 1.25
        else:
            print(f'seu salario é {salatual} e você não teve aumento')
            exit()
    else:
        print('ERRO!!! salario atual negativo')
    if tempo > 0:
        if tempo < 10:
            if (tempo >= 10) and (tempo <= 7):
                novo += 300
            if (tempo >= 4) and (tempo <= 6):
                novo += 200
            if (tempo >= 1) and (tempo <= 3):
                novo += 100
            if tempo < 1:
                print('Sem bônus!!!')
        else:
            novo += 500
    else:
        print('Tempo inválido')
    print(f'O salario reajustado: {round(novo, 2)}')
except ValueError:
    print('ERRO!!!')