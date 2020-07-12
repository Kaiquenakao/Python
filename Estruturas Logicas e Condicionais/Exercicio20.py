""""
20. Dados três valores A, B, C, verificar se eles podem ser valores dos lados de um triangulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes
conceitos:
    * O comprimento de cada lado do triângulo é menor do que a soma dos outros dois lados
    * Chama-se equilátero o triângulo que tem três lados iguais.
    * Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    * Recebe o nome de escaleno o triângulo que tem três lados diferentes.
"""
try:
    A = float(input('Insira o valor do lado A:  '))
    B = float(input('Insira o valor do lado B:  '))
    C = float(input('Insira o valor do lado C:  '))
    if (A < (B + C)) and (B < (A + C)) and (C < (A + B)):
        if A == B and C == B and A == C:
            print('Triângulo equilátero')
            exit()
        if A == B or B == C or A == C:
            print('Triângulo isóceles')
        else:
            print('Triângulo Escaleno')
    else:
        print('Não é um triangulo')

except ValueError:
    print('ERRO!! Só pode ser digitados números')