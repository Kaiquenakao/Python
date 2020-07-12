"""
23. Leia um valor de área em metro quadrados m² e apresente-o convertido em jardas. A fórmula
de conversão é: J = M / 0.91, sendo J o comprimento em jardas e M o comprimento em metro.
"""
M = float(input('Insira o seu valor em metro quadrados para converter em jardas:   '))
J = M / 0.91
print(f'O seu valor convertido em jardas: {round(J, 3)}')