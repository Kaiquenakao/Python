"""
49. Faça um programa para leia o horário (hora, minuto, segundo) de ínicio e a duração, em
segundos, de uma experiência biológica. O programa deve resultar como o novo horário
(hora, minuto e segundo) do termino da mesma.
"""
import datetime
try:
    hora = int(input('Insira as horas:  '))
    minuto = int(input('Insira os minutos:  '))
    segundo = int(input('Insira os segundos:  '))
    duracao = int(input('Insira a duracao:  '))
    x = datetime.timedelta(hours=hora,  minutes=minuto, seconds=segundo)
    novo = x + datetime.timedelta(seconds=duracao)
    print(f'O inicio: {x}\nO fim: {novo}')
except ValueError:
    print('ERRO!!! só pode ser digitados números inteiros')