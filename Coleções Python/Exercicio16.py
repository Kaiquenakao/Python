"""
16. Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro.
Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta, se for 2,
mostre o vetor na ordem inversa. Caso, o código for diferente de 1 e 2 escreva uma mensagem informado
que o código é inválido
"""
lista = []

for i in range(1, 6+1):
    if i == 6:
        cod = int(input('0 - Finaliza o programa\n1 - Ordem direta\n2 - Ordem inversa\nInsira um número:  '))
        if (cod >= 0) and (cod <= 2):
            if cod == 0:
                print(f'Programa finalizado!!!')
                break
            if cod == 1:
                print(f'Lista ordem direta: {sorted(lista)}')
                break
            if cod == 2:
                print(f'Lista ordem inversa: {sorted(lista[::-1])}')
                break
    n = float(input(f'{i} - Insira um número:  '))
    lista.append(n)

