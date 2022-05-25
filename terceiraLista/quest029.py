'''
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca
de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele 
desenvolveu um tabela que contém o número de itens que o cliente comprou e ao
lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar 
quantos itens o cliente está levando e olhar na tabela de preços 
Você foi contratado para desenvolver o programa que monta esta tabela de preços
que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

    Lojas Quase Dois - Tabela de preços
    1 - R$ 1.99
    2 - R$ 3.98
    ...
    50 - R$ 99.50
'''

quantidade = int(input('Insira a quantidade de itens comprados: '))
if quantidade < 50 and quantidade > 0:
    preco_item = 1.99
    for i in range(1, quantidade+1):
        print(f'{i} - {preco_item:.2f} R$')
        preco_item += 1.99
    print(f'Preço a ser pago: {quantidade*1.99:.2f} R$')
else:
    print('Máximo até 50 itens.')
