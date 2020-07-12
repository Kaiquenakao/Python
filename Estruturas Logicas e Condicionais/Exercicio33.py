"""
33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule
e escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda
tabela)
----------------------------------------------------------
|    Preço antigo       |     Percentual de aumento      |
| até R$ 50             |             5%                 |
| entre R$ 50 e R$ 100  |            10%                 |
| acima R$ 100          |            15%                 |
----------------------------------------------------------

----------------------------------------------------------------------
|    Preço Novo                     |            Mensagem            |
| até R$ 80                         |            Barato              |
| entre R$ 80 e R$ 120 (inclusive)  |            Normal              |
| entre R$ 120 e R$ 200 (inclusive) |            Caro                |
| Acima de R$ 200                   |            Muito caro          |
----------------------------------------------------------------------
"""
try:
    preco = float(input('Insira o preço antigo:  '))

    if (preco > 0) and (preco <= 50):
        novo = preco * 1.05
    if (preco > 50) and (preco < 100):
        novo = preco * 1.10
    if preco >= 100:
        novo = preco * 1.15
    if (novo > 0) and (novo <= 80):
        print(f'O preço: {round(novo,2)}\nBarato!!!')
    if (novo > 80) and (novo < 120):
        print(f'O preço novo: {round(novo,2)}\nNormal!!!')
    if (novo >= 120) and (novo < 200):
        print(f'O preço novo: {round(novo,2)}\nCaro!!!')
    if novo > 200:
        print(f'O preço {round(novo,2)}\nMuito Caro!!!')
except ValueError:
    print('ERRO!!! Só pode ser digitado números')