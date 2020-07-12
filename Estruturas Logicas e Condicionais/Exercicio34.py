"""
34. Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a
tabela abaixo , quando o aluno tem mais de 20 faltas ocorre a redução de conceito.
--------------------------------------------------------------------------------
|     Nota       |    Conceito (Até 20 faltas)  | Conceito (Mais de 20 faltas  |
| 9.0 até 10.0   |            A                 |              B               |
| 7.5 até 8.9    |            B                 |              C               |
| 5.0 até 7.4    |            C                 |              D               |
| 4.0 até 4.9    |            D                 |              E               |
| 0.0 até 3.9    |            E                 |              E               |
"""
try:
    faltas = int(input('Insira a quantidade de falta:  '))
    nota = float(input('Insira a nota:  '))
    if (nota > 0) and (nota <= 10):
        if (faltas > 0) and (faltas <= 20):
            if (nota > 0) and (nota <= 3.9):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito E')
            if (nota >= 4.0) and (nota <= 4.9):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito D')
            if (nota >= 5.0) and (nota <= 7.4):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito C')
            if (nota >= 7.5) and (nota <= 8.9):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito B')
            if (nota >= 9.0) and (nota <= 10.0):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito A')
        if faltas > 20:
            if (nota > 0) and (nota <= 3.9):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito E')
            if (nota >= 4.0) and (nota <= 4.9):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito E')
            if (nota >= 5.0) and (nota <= 7.4):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito D')
            if (nota >= 7.5) and (nota <= 8.9):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito C')
            if (nota >= 9.0) and (nota <= 10.0):
                print(f'Você tem {faltas} faltas e a sua nota é {nota}\nConceito B')
    else:
        print('NOTA INVÁLIDA')
except ValueError:
    print('ERRO!!! A Nota tem que ser números float/inteiro, e a falta tem que ser número inteiro')
