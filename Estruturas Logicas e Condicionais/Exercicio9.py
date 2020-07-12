"""
9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação
for maior que 20% do salário imprima:Emprestimo não concedido, Caso contrário imprima:
Empréstimo concedido
"""
salario = float(input('Insira o salário do trabalhador:'))
prestacao = float(input('Insira o valor da prestação'))
print(((prestacao * 100) / salario))
if ((prestacao * 100) / salario) > 20:
    print('Emprestimo não concedido')
else:
    print('Empréstimo concedido')