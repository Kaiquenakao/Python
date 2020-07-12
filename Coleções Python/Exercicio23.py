"""
23. Ler dois conjuntos de números reais, armazenando-o em vetores e calcular o produto escalar entre
eles. Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o
produto escalar é dado por: x1 * y1 + x2 * y2 +...+xn * yn.
"""
vetorA = []
vetorB = []
vetorC = []

print('Vetor 1')
for i in range(0, 4+1):
    n = float(input(f'{i + 1} - Insira um número:  '))
    vetorA.append(n)

print('Vetor 2')
for i in range(0, 4+1):
    n = float(input(f'{i + 1} - Insira um número:  '))
    vetorB.append(n)

print('Vetor escalado')
for i in range(0, 4+1):
    c = vetorA[i] * vetorB[i]
    vetorC.append(c)

print(f'Vetor 1:  {vetorA}\nVetor 2:  {vetorB}\nVetor escalado:  {vetorC}')