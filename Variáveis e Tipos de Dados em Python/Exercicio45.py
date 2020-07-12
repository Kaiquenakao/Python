"""
45. Faça um programa para converter uma letra maiúscula em letra minúscula.
"""
try:
    letra = input('Insira uma letra maíuscula:  ')
    print(f'Convertendo para letra minúscula: {letra.lower()}')
except ValueError:
    print('ERRO!!! só pode ser digitado letra minúscula')