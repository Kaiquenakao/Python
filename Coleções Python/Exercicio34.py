"""
34. Faça um programa para ler 10 números diferentes a serem armazenados em um vetor. Os dados deverão
ser armazenados no vetor na ordem que forem lidos, sendo que caso o usuário digite um número que já
foi digitado anteriormente, o programa deverá pedir para ele digitar outro número. Note que cada
valor digitado pelo usuário deve ser pesquisado no vetor, verificando se ele existe entre os números
que já foram fornecidos. Exibir na tela o vetor final que foi digitado
"""
vetor = []
contador = 0

while contador < 10:
    n = float(input(f'{contador+1} - Insira um número (que não esteja no vetor):  '))
    if n not in vetor:
        vetor.append(n)
        contador = contador + 1
    else:
        print('Valor já está no vetor')

print(vetor)