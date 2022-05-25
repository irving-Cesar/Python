'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
e agora possui uma loja de conveniências. Faça um programa que implemente uma 
caixa registradora rudimentar. O programa deverá receber um número desconhecido 
de valores referentes aos preços das mercadorias. Um valor zero deve ser informado
pelo operador para indicar o final da compra. O programa deve então mostrar o
total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco. Após esta operação, o programa 
deverá voltar ao ponto inicial, para registrar a próxima compra

A saída deve ser conforme o exemplo abaixo:
    Lojas Tabajara 
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00 -> 8.0?
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
'''

preco_produto = 1
cont_i = 1
total = 0
troco = 0
add_troco = 0
while preco_produto < 0 or preco_produto != 0:
    preco_produto = float(input(f'Produto {cont_i}: R$ '))
    if preco_produto != 0:
        total += preco_produto
    else:
        print(f'Total: {total} R$')
        dinheiro = float(input('Dinheiro: R$ '))
        troco = dinheiro - total
        if troco < 0:
            while troco < 0:
                print(f'Faltam: R$ {troco * (-1):.2f}')
                add_troco = float(input('Valor que falta: '))
                troco += add_troco
                
                if troco > 0:
                    print(f'Troco: R$ {troco:.2f}')
        else:
            print(f'Troco: R$ {troco:.2f}')
            
    cont_i += 1
