"""
59. Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor de kwh, e
para cada habitante entre com os seguintes dados: consumo do mês e o código do consumidor 1
(1- Residencial, 2 - Comercial, 3 - Industrial). no final imprima o maior, o menor e a média
do consumo dos habitantes; e por fim o total do consumo de cada categoria de consumidor.
"""
import statistics
habitantes = int(input('Insira o número de habitantes:  '))
kwh = float(input('Insira o valor do kwh:  '))
listaconsumo = []
residencial = []
comercial = []
industrial = []
for i in range(1, habitantes+1):
    consumo = float(input(f'Habitante {i} - Qual foi o seu consumo:  '))
    listaconsumo.append(consumo * kwh)
    categoria = int(input(f'1 - Residencial\n2 - Comercial\n3 - Industrial\nSelecione a sua categoria:  '))
    if (categoria > 0) and (categoria <= 3):
        if categoria == 1:
            residencial.append(consumo * kwh)
        if categoria == 2:
            comercial.append(consumo * kwh)
        if categoria == 3:
            industrial.append(consumo * kwh)
    else:
        print('ERRO!!!')
        break
print(f'O maior consumo foi: {max(listaconsumo)}\nO menor consumo foi: {min(listaconsumo)}\nA media do '
      f'Consumo é {statistics.mean(listaconsumo)}')
print(f'Total do consumo categoria industrial: {sum(industrial)}\nTotal do consumo categoria comercial: {sum(comercial)}'
      f'\nO total do consumo categoria residencial: {sum(residencial)}')