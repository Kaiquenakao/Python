"""
14. Leia um ângulo em graus e apresente-o convertido em radiano. A fôrmula de conversão
é R = G * pi / 180, sendo G o ângulo em graus e R em radianos e pi = 3,14.
"""
import math
G = float(input('Insira o seu valor em graus para converter ele em radiano:'))
R = G * math.pi / 180
print(f"O seu valor convertido em radianos:{R}")