"""
38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros:
Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma data válida. Teste
se o dia fornecido é um dia válido: dia > 0 ≤ 28 para o mês de fevereiro (29 se o ano for
bissexto), dia ≤ 30 em abril, junho, setembro e novembro, se dia ≤ 31 nos outros meses. Teste
a validade do mês: mês > 0 e mês < 13. Teste a validade do ano: ano ≤ ano atual (use uma
constante definida com o valor igual a 2008). Imprimir: "data válida" ou "data inválida"
no final da execução do programa.
"""
x = 2020
try:
    dias, mes, ano = [int(x) for x in input('Insira a data,mes e o ano, por exemplo 30/03/1998: ').split('/')]
    if ano <= x:
        if (mes > 0) and (mes <= 12):
            if mes == 1:
                if (dias > 0) and (dias <= 31):
                    print('Você escolheu Janeiro')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 2:
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
            if mes == 3:
                if (dias > 0) and (dias <= 31):
                    print('Você escolheu Março')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 4:
                if (dias > 0) and (dias <= 30):
                    print('Você escolheu Abril')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 5:
                if (dias > 0) and (dias <= 31):
                    print('Você escolheu Maio')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 6:
                if (dias > 0) and (dias <= 30):
                    print('Você escolheu Junho')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 7:
                if (dias > 0) and (dias <= 31):
                    print('Você escolheu Julho')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 8:
                if (dias > 0) and (dias <= 31):
                    print('Você escolheu Agosto')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 9:
                if (dias > 0) and (dias <= 30):
                    print('Você escolheu Setembro')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 10:
                if (dias > 0) and (dias <= 31):
                    print('Você escolheu Outubro')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 11:
                if (dias > 0) and (dias <= 30):
                    print('Você escolheu Novembro')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
            if mes == 12:
                if (dias > 0) and (dias <= 31):
                    print('Você escolheu Dezembro')
                    print(f'O dia {dias} existe!!!')
                else:
                    print('Dia inválido')
        else:
            print('Mês Inválido')
    else:
        print('Ano inválido!!!')
except ValueError:
    print('ERRO!!! Só pode ser digitado números inteiros')
