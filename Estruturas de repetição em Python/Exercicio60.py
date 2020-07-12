"""
60. Faça um programa que leia vários números, calcule e mostre:

(a) A soma dos números digitados
(b) A quantidade de números digitados
(c) A média dos números digitados
(d) O maior número digitado
(e) O menor número digitados
(f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.
"""
soma = 0
digitados = 0
lista = []
listapar = []
par = 0
while True:
    a = float(input('Insira um número:  '))
    if a == 0:
        print('Programa finalizado!!!')
        break
    else:
        soma = soma + a
        digitados = digitados + 1
        lista.append(a)
        if a % 2 == 0:
            listapar.append(a)
            par = par + 1
print(f'A soma dos números digitados: {soma}\nA quantidade de número: {digitados}\nA media dos números '
      f'digitados: {soma / digitados}\nO maior número digitado: {max(lista)}\nO menor número digitado:  {min(lista)}\n'
      f'A média dos números pares: {sum(listapar) / par}')