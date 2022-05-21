'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 
Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

print('''-----------     Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg''')
print('')
print ('F - File Duplo\nA - Alcatra\nP - Picanha\n')

tipo_carne = str(input('Insira o tipo da carne: '))
quantidade_carne = float(input('Insira os kg: '))
possui_cartao = str(input('Possui cartão da loja?\nS - sim\nN - não\n'))

tipo_carne = tipo_carne.lower()
possui_cartao = possui_cartao.lower()

cartao = True if possui_cartao == 's' else False
tipo_pagamento = 'Cartão loja' if cartao else 'Dinheiro'

desc_valor = 0
desc = ''

preco_file = 0
preco_alcatra = 0
preco_picanha = 0

preco_total = 0

if tipo_carne == 'f':
    tipo_carne = 'Filé Duplo'
    if quantidade_carne <= 5:
        preco_file = 4.9
    else:
        preco_file = 5.8
    preco_total = quantidade_carne * preco_file
    if cartao:
        desc = '(-5%)'
        desc_valor = (preco_total * 0.05)
        
elif tipo_carne == 'a':
    tipo_carne = 'Alcatra'
    if quantidade_carne <= 5:
        preco_alcatra = 5.9
    else:
        preco_alcatra = 6.8
    preco_total = quantidade_carne * preco_alcatra
    if cartao:
        desc = '(-5%)'
        desc_valor = (preco_total * 0.05)
        
elif tipo_carne == 'p':
    tipo_carne = 'Picanha'
    if quantidade_carne <= 5:
        preco_picanha = 6.9
    else:
        preco_picanha = 7.8
    preco_total = quantidade_carne * preco_picanha
    
    if cartao:
        print('passou')
        desc = '(-5%)'
        desc_valor = (preco_total * 0.05)

print(f'Carne: {tipo_carne}\nQuantidade (Kg): {quantidade_carne}\nPreco total (sem desconto): {preco_total} R$\nForma de pagamento: {tipo_pagamento}\nValor do desconto: {desc_valor} R$\nValor final {desc}: {(preco_total - desc_valor):.2f} R$')
    
