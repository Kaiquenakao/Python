"""
33. Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem
crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. exemplo:
Para n = 6, i = 2 e j = 3 a saída deverá ser: 0,2,3,4,6,8
"""
try:
    lista = []
    contador = 0
    mult2 = 1
    mult3 = 0

    n = int(input('Insira um número positivo para N vezes números múltiplos:  '))
    while n > contador:
        lista.append(mult3)
        mult3 = mult3 + 3
        contador = contador + 1
        if n > contador:
            mult2 = mult2 * 2
            lista.append(mult2)
            contador = contador + 1
    print(lista)
except ValueError:
    print('ERRO!!!! Número inválido')