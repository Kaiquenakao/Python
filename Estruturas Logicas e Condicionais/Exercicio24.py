"""
24. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma
taxa diferente imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa
em que o usuário entre com o valor e o estado Destino do produto e o programa retorne o preço
final do produto acrescido do imposto do estado em que ele será vendido. Se o  número do
estado digitado não for válido, mostrar uma mensagem de erro.
"""
try:
    estado = int(input(
        'Estados:\n1- Minas Gerais (MG)\n2 - São Paulo (SP)\n3 - Rio de Janeiro (RJ)\n'
        '4 - Mato Grosso do Sul (MS)\nDigite a opção:    '
    ))
    if (estado > 0) and (estado <= 4):
        valor = float(input('Insira o valor do produto:  '))
        if estado == 1:
            print(f'Você escolheu Minas Geras, O imposto de MG é 7%\nO resultado final {"%.2f" % (valor * 1.07)}')
        if estado == 2:
            print(f'Você escolheu São Paulo, O imposto de SP é 12%\nO resultado final {"%.2f" % (valor * 1.12)}')
        if estado == 3:
            print(f'Você escolheu Rio de Janeiro, O imposto de RJ é 15%\nO resultado final {"%.2f" % (valor * 1.15)}')
        if estado == 4:
            print(f'Você escolheu Mato Grosso do sul, O imposto de MS é 8%\nO resultado final {"%.2f" % (valor * 1.08)}')
    else:
        print('ERRO!!!')
except ValueError:
    print('ERRO!!! Só pode ser digitado números')
