"""
36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números
naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números naturais é:
    1² + 2² + 3² +...+ 10² = 385

O quadrado da soma dos dez primeiros número naturais, é
    (1 + 2 +...+ 10)² = 552 = 3025
"""
try:
    somaquadrado = 0
    quadradosoma = 0
    for i in range(1, 100+1):
        somaquadrado = (i * i) + somaquadrado
    for i in range(1, 100+1):
        quadradosoma += i
    print(f'A diferença entre a soma dos quadrados: {somaquadrado} menos o quadrado da soma'
          f' {quadradosoma * quadradosoma} '
          f'é = {(quadradosoma * quadradosoma) - somaquadrado}')
except ValueError:
    print('ERRO!!!')