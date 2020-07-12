"""
4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores
X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá
escrever a soma dos valores encontrados nas respectivas posições X e Y
"""
lista = []
for i in range(1,8+1):
    if i == 1:
        x = int(input(f'Insira a posição do vetor X:'))
        y = int(input(f'Insira a posição do vetor Y:'))
    valor = float(input(f'Posição{i}:insira o valor:'))
    lista.append(valor)
print(f'A soma da posição X{x}:{lista[x-1]} + Y{y}:{lista[y-1]} igual: {lista[x-1] + lista[y-1]}')

