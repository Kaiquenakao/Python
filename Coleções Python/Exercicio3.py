"""
3. Ler um conjunto de números reais, armazenando-o em vetor e calcular a raiz quadrado das componentes
deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada
. imprimir todos os conjuntos.
"""
import math
calcular = []
valores = []
for num in range(1,10+1):
    numeros = int(input(f'Posição{num}:Insira um valor:'))
    valores.append(numeros)
print(f'Vetor de valores{valores}')
for num in valores:
    raiz = math.sqrt(num)
    calcular.append(raiz)
print(f'Vetor das raizes quadradas:{calcular}')

