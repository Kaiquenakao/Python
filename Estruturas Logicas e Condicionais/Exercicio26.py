"""
26. Leia a distância em Km e a quantidade de litros de gasolina consuminados por um carro
em um percurso, calcule o consumo em Km/L e escreva uma mensagem de acordo com a tabela
abaixo:
----------------------------------------------
| CONSUMO    | (Km/l) |   MENSAGEM           |
| Menor que  |   8    |    Venda o carro!    |
| Entre      | 8 e 14 |    Econômico         |
| Maior que  |   12   |    Super econômico   |
"""
try:
    km = float(input('Insira a distância em KM:  '))
    litros = float(input('Insira a quantidade de litros de gasolina:  '))
    kml = km / litros
    if kml < 8:
        print('Venda o carro!')
    if (kml > 8) and (kml < 14):
        print('Econômico')
    if kml > 12:
        print('Super econômico')
except ValueError:
    print('ERRO!!! Só pode ser digitado números')