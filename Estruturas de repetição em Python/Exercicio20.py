"""
20. Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser
informado o número de dados lidos e número de valores pares. O processo termina quando
for digitado o número 1000
"""
try:
    dados = 0
    valores = 0
    lista = []
    qnt = int(input('Insira a quantidade de sequência:  '))
    for i in range(1, qnt + 1):
        num = int(input(f'{i} - Insira um número:  '))
        if num != 1000:
            dados = dados + 1
            if num % 2 == 0:
                valores = valores + 1
                lista.append(num)
        else:
            print('Processo terminado!!!')
            break
    print(f'Dados lidos: {dados}\nNumero de pares: {valores}\nLista de números pares inseridos {lista}')
except ValueError:
    print('ERRO!!!')
