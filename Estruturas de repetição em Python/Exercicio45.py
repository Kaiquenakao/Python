"""
45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa.
você deve criar um menu com duas opções de conversão e com uma opção para finalizar o programa
O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado
quando a opção de finalizar for escolhida.
"""
while True:
    opcao = int(float(input('Opções\n1 - converter km/h para m/s\n2 - converter m/s para km/h\n'
                            '3 - finalizar o programa\n'
                            'Digite a opção:  ')))
    if opcao == 1:
        km = float(input('Insira o valor do km/h:  '))
        print(f'O valor convertido para m/s: {km / 3.6}')
    if opcao == 2:
        ms = float(input('Insira o valor do m/s:  '))
        print(f'O valor convertido para km/h: {ms * 3.6}')
    if opcao == 3:
        print('Programa finalizado')
        break
    if (opcao < 0) or (opcao > 3):
        print('Valor inválido. tente novamente')