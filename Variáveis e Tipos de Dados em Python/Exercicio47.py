""""
47. Leia um número inteiro de 4 dígito (de 1000 a 9999) e imprima 1 digíto por linha.
"""
try:
    num = int(input('Insira 4 dígito de 1000 a 9999:  '))
    x = str(num)
    if (num >= 1000) and (num <= 9999):
        for i in x:
            print(int(i))
    else:
        print('ERRRO!! O valor tem que ser de 1000 a 9999')
except ValueError:
    print('ERRO!! Só pode ser digitado número inteiros')