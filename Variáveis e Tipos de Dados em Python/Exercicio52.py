"""
52. Três amigos jogaram na loteria. Caso eles ganhem o prêmio deve ser repartido proporcio
nalmente ao valor de cada deu para realização da aposta. Faça um programa que leia quanto
cada apostador investiu , o valor do prêmio, e imprima quanto cada ganharia do prêmio
com base no valor investido.
"""
try:
    apos1 = float(input('Quanto o primeiro apostador investiu:  '))
    apos2 = float(input('Quanto o segundo apostador investiu:  '))
    apos3 = float(input('Quanto o terceiro apostador investiu:  '))
    premio = float(input('Qual é o valor do premio:  '))
    apostaTotal = apos1 + apos2 + apos3
    p1 = apos1 / apostaTotal
    p2 = apos2 / apostaTotal
    p3 = apos3 / apostaTotal
    print(f'O primeiro apostador ganharia: {p1 * premio}\n'
          f'O segundo apostador ganharia: {p2 * premio}\n'
          f'O terceiro apostador ganharia: {p3 * premio}')
except ValueError:
    print('ERRO!!!!! Só pode ser digitado números')


