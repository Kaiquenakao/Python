"""
51. Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule a distância
da origem (0, 0)
"""
import math
try:
    x = float(input('Insira a coordenadas do x:  '))
    y = float(input('Insira a coordenadas do y:  '))
    R = math.sqrt(pow(x, 2) + pow(y, 2))
    print(f'A distância de origem é {"%.2f" % R}')
except ValueError:
    print('ERRO!!!! só pode ser digitados números')