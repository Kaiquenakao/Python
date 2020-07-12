"""
29. Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros
menores do que 100. escolha números aleatórios entre 1 e 100, e moestre na tela a pergunta:
qual é a soma de a + b, onde a e b são os números aleatórios. peça a respota. Faça cinco
perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas
vezes o aluno acertou.
"""
import random
try:
    contador = 0
    for i in range(5):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        soma = a + b
        print(f'Qual é a soma de {a} + {b}?')
        resp = int(input('Insira a resposta:  '))
        if resp == soma:
            print('Você acertou!!!')
            contador += 1
    print(f'Você acertou {contador} vezes')
except ValueError:
    print('ERRO!!! Só pode ser digitado números')