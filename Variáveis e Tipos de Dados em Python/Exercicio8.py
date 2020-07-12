"""
8 - Leia um temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A fórmula para conversão é C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura
Kelvin
"""
K = float(input("Insira o seu valor em temperatura Kelvin para converter para Graus Celsius:"))
C = K - 273.15
print(f"A sua conversão para Graus Celsius:{C}")