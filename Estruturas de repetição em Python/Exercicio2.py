"""
2. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 3 vezes. A primeira
vez deve usar a estrutura de repetição for, a segunda while, e a terceira do while.
"""
for num in range(1,100+1):
    print(num)

global contador
contador = 1
while(contador <= 100):
    print(contador)
    contador = contador + 1