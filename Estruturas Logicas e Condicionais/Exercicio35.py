"""
35. Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre
1 e 12, e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos,
28 dias em anos não bissextos.
"""
opcao = int(input(''
                  '1 - Janeiro\n'
                  '2 - Fevereiro\n'
                  '3 - Março\n'
                  '4 - Abril\n'
                  '5 - Maio\n'
                  '6 - Junho\n'
                  '7 - Julho\n'
                  '8 - Agosto\n'
                  '9 - Setembro\n'
                  '10 - Outubro\n'
                  '11 - Novembro\n'
                  '12 - Dezembro\n'
                  'Escolha uma opção:  '))
if (opcao > 0) and (opcao <= 12):
    ano = int(input('Insira um ano:  '))
    dias = int(input('Insira o dia:  '))
    if opcao == 1:
        if (dias > 0) and (dias <= 31):
            print('Você escolheu Janeiro')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 2:
        if (ano % 4 == 0) or (ano % 400 == 0) and not (ano % 100 == 0):
            if (dias > 0) and (dias <= 29):
                print(f'Você escolheu Fevereiro\nO ano {ano} é bissexto\nO dia {dias} existe!!!')
                exit()
            else:
                print('Dia invalido')
        else:
            if (dias > 0) and (dias <= 28):
                print(f'Você escolheu Fevereiro\nO dia {dias} existe!!!')
            else:
                print('Dia invalido')
    if opcao == 3:
        if (dias > 0) and (dias <= 31):
            print('Você escolheu Março')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 4:
        if (dias > 0) and (dias <= 30):
            print('Você escolheu Abril')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 5:
        if (dias > 0) and (dias <= 31):
            print('Você escolheu Maio')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 6:
        if (dias > 0) and (dias <= 30):
            print('Você escolheu Junho')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 7:
        if (dias > 0) and (dias <= 31):
            print('Você escolheu Julho')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 8:
        if (dias > 0) and (dias <= 31):
            print('Você escolheu Agosto')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 9:
        if (dias > 0) and (dias <= 30):
            print('Você escolheu Setembro')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 10:
        if (dias > 0) and (dias <= 31):
            print('Você escolheu Outubro')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 11:
        if (dias > 0) and (dias <= 30):
            print('Você escolheu Novembro')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
    if opcao == 12:
        if (dias > 0) and (dias <= 31):
            print('Você escolheu Dezembro')
            print(f'O dia {dias} existe!!!')
        else:
            print('Dia inválido')
else:
    print('Opção Inválida')
