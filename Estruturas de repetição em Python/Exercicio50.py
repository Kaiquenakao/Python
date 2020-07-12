"""
50. Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e
cresce 3 centímetros por ano. Escreva um programa que calcule e imprima quantos anos serão
necessários para que Zé seja maior que Chico
"""

chico = 1.50
ze = 1.10
ano = 1

while True:
    chico = chico + 0.02
    ze = ze + 0.03
    ano = ano + 1
    if ze > chico:
        print(f'Anos necessário {ano}')
        break
