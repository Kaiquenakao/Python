"""
6 - Leia um temperatura em graus Celsius e apresente-se a convertida em graus Fahrenheit.
a fórmula para conversão é F = C * (9.0/5.0) + 32.0, sendo F a temperatura Fahrenheit e
C a temperatura em Celsius
"""
C = float(input("Insira o seu valor em Graus celsius para converter para graus Fahrenheit:"))
F = C * (9.0/5.0) + 32.0
print(f"O seu valor convertido para Graus Fahrenheit:{F}")