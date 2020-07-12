"""
43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
* o total a pagar com desconto de 10%;
* o total de cada parcela, no parcelamento de 3x sem juros;
* A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
* A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total);
"""
try:
    salario = float(input('Insira o valor total:  '))
    print(f'o total a pagar com desconto de 10%: {salario - (salario * 0.10)}')
    print(f'o total de cada parcela, no parcelamento de 3x sem juros: {round(salario / 3, 2)}')
    print(f'A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto): {(salario - (salario * 0.10)) * 0.05}')
    print(f'A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total): {salario * 0.05}')
except ValueError:
    print(f'ERRO!!! Só pode ser digitado números')