"""
15. Leia um ângulo em radianos e apresente-a convertido em graus. A fôrmula da conversão
é: G = R * 180 / pi, sendo G o ângulo em graus e R em radianos e pi = 3.14.
"""
import math
R = float(input('Insira o valor do seu ângulo em radianos para converter ele em graus:'))
G = (R * 180) / math.pi
print(f'O seu valor convertido em graus:{G}')