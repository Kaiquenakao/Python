"""
37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem
a propriedade seguinte: A soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais
alta ordem elevada ao quadrado é igual ao próprio numero. Por exemplo, para o número inteiro
3025, temos que:
30 + 25 = 55
55 = 3025
"""
for i in range(1000, 9999+1):
    part1 = round((i / 100))
    part2 = (i % 100)
    final = pow((part1 + part2), 2)
    if final == i:
        print(f'{part1} + {part2} = {part1 + part2} > {part1 + part2}² = {final}')