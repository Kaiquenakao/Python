"""
38. Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores,
guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao final da tela os valores
em ordem
"""
vetor = []

for i in range(0, 9+1):
    n = float(input(f'{i+1} - Insira um número:  '))
    vetor.append(n)
    x = sorted(vetor)
print(x)