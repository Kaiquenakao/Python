"""
7 - Leia uma temperatura em graus Fahrenheit e apresente-se a convertida em graus Celsius.
a fórmula é: C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius e F a temperatura
Fahrenheit
"""
F = float(input("Insira o seu valor em Graus Fahrenheit para converter para Graus Celsius:"))
C = 5.0 * (F - 32.0) / 9.0
print(f"O seu valor convertido para Graus Celsius {C}")