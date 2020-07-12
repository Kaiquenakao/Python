"""
29. Faça um programa que receba 6 números inteiros e mostre:
    • Os números pares digitados;
    • A soma dos números pares digitados;
    • Os números ímpares digitados;
    • A quantidade de números ímpares digitados;
"""
listapar = []
listaimpar = []
qnt = 0

for i in range(0, 5+1):
    n = int(input(f'{i+1} - Insira um número:  '))
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
        qnt = qnt + 1

print(f'Número pares digitados: {listapar}\nA soma dos números pares digitados:  {sum(listapar)}\n'
      f'Os números ímpares digitados: {listaimpar}\nA quantidade de números ímpares digitados: {qnt}')
