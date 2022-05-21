'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
for p in range(1, 4):
    preco = float(input('Insira o {}° preço: '.format(p)))
    if p == 1:
        preco_menor = preco

    if preco < preco_menor:
        preco_menor = preco
    
print('Compre o de {} R$.'.format(preco_menor))
