"""
1. Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O
Programa deve executar os seguintes passos
(a) Atribua os seguintes valores a esses vetor:1,0,5,-2 ,-5,7;
(b) Armazene em uma variável inteira(simples) a soma entre os valores da posições A[0], A[1]
e A[5] do vetor e mostre na tela esta soma;
(c) Modifique o vetor na posição 4, atribuindo a está posição o valor 100;
(d) Mostre na tela cada valor do vetor A, um em cada linha;
"""
#(a) Atribua os seguintes valores a esses vetor:1,0,5,-2 ,-5,7;
A = [1,0,5,-2,-5,7]
"""(b) Armazene em uma variável inteira(simples) a soma entre os valores da posições A[0], A[1]
e A[5] do vetor e mostre na tela esta soma;"""
soma = A[0] + A[1] + A[5]
print(f'A soma:{soma}')
"""
(c) Modifique o vetor na posição 4, atribuindo a está posição o valor 100;
"""
A[4] = 100
print(f'Posição 4 modificada:{A[4]}')
"""
(d) Mostre na tela cada valor do vetor A, um em cada linha;
"""
for num in A:
    print(num)