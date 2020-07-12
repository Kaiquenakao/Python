"""
19. Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * 1) % (i + 1), sendo i
a posição elemento no vetor. em seguida imprima o vetor na tela.
"""
lista = []
for i in range(1, 50+1):
    lista.append(((i + 5 * 1) % (i + 1)))
print(lista)