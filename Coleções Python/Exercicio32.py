"""
32. Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa
elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo:
    • Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição y
    • Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição em y.
    • Diferença entre x e y: todos os elementos de x que não existam em y.
    • Intersecção entre x e y: apenas os elementos que aparecem nos dois vetores.
    • União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.

    print('Vetor x')
for i in range(0, 3):
    n = int(input(f'{i} - Insira um número:  '))
    x.append(n)
print('Vetor y')
for i in range(0, 3):
    n = int(input(f'{i} - Insira um número:  '))
    y.append(n)
"""
x = []
y = []
vetorsoma = []
vetorproduto = []
vetordiferenca = []
vetorinteseccao = []
cont = 0

print('Vetor x')

while cont <= 9:
    n = int(input(f'{cont + 1} - Insira um número (não existente no vetor):  '))
    if n not in x:
        x.append(n)
        cont = cont + 1
    else:
        print('ERRO!!! Número já existente')

cont = 0
print('Vetor y')

while cont <= 9:
    n = int(input(f'{cont + 1} - Insira um número (não existente no vetor):  '))
    if n not in y:
        y.append(n)
        cont = cont + 1
    else:
        print('ERRO!!! Número já existente')

for i in range(0, 9+1):
    soma = x[i] + y[i]
    vetorsoma.append(soma)

for i in range(0, 9+1):
    produto = x[i] * y[i]
    vetorproduto.append(produto)

for i in x:
    if i not in y:
        diferenca = i
        vetordiferenca.append(diferenca)

X = set(x)
Y = set(y)

print(f'Vetor x: {x}\nVetor y: {y}\nVetor soma: {vetorsoma}\nVetor produto: {vetorproduto}\n'
      f'Vetor diferença: {vetordiferenca}\nVetor intersecção: {X.intersection(Y)}\nVetor União: {X.union(Y)}')


