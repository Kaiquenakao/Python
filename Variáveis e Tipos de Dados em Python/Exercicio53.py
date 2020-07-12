"""
53. Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como
preço do metro de tela p. imprima o custo para  cercar este mesmo terrreno com tela.
"""
try:
    c = float(input('Insira o comprimento:  '))
    v = float(input('Insira a largura:  '))
    area = v * c
    p = float(input('Insira o preço por metro de tela:  '))
    print(f'A área do terreno: {area}\nO custo para cercar todo o terreno com tela: {area/p} reais')
except ValueError:
    print('ERRO!!! Só pode ser digitado números')