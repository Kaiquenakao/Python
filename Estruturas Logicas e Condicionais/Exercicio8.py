"""
8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba
na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre
0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao
usuário e o programa termina.
"""
num1 = float(input('Insira a sua primeira nota:'))
num2 = float(input('Insira a sua segunda nota:'))
if num1 >= 0 and num1 <= 10 and num2 >= 0 and num2 <= 10:
    print(f'Sua média:{(num1 + num2) / 2}')
else:
    print('Valor inválido, não está na faixa de 0.0 a 10.0')