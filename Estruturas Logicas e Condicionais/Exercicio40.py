"""
40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do
distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica,
de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.
------------------------------------------------------------------------------
|     Custo de fábrica           |    % do Distribuidor   | % dos impostos   |
| até R$ 12.000,00               |           5            |      isento      |
| entre R$ 12.000,00 e 25.000,00 |          10            |        15        |
| acima de R$ 25.000,00          |          15            |        20        |
"""
try:
    fabrica = float(input('Insira o custo de fábrica:  '))
    if fabrica > 0:
        if (fabrica > 0) and (fabrica <= 12000):
            dis = fabrica + (fabrica * 5 / 100)
            total = dis + fabrica
        if (fabrica > 12000) and (fabrica < 25000):
            dis = fabrica + (fabrica * 10 / 100)
            imposto = fabrica + (fabrica * 15 / 100)
            total = dis + imposto + fabrica
        if fabrica > 25000:
            dis = fabrica + (fabrica * 15 / 100)
            imposto = fabrica + (fabrica * 20 / 100)
            total = dis + imposto + fabrica
    else:
        print('Número negativo')
    print(f'O custo para consumidor: {total}')
except ValueError:
    print('ERRO!!!! Só pode ser digitado números.')