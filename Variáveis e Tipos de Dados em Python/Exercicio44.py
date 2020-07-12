"""
44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo
a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir o seu objetivo
"""
try:
    altura = int(input('Insira a altura do degrau:  '))
    escada = int(input('Insira a altura que você deseja alcançar:  '))
    print(f'você deverá subir {escada / altura} degraus')
except ValueError:
    print(f'ERRO!!! só pode ser digitado números inteiro')