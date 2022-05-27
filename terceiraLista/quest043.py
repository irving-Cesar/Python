'''
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
geral do pedido. Considere que o cliente deve informar quando o pedido deve ser 
encerrado
'''

cardapio = [
    {'nome': 'Cachorro Quente', 'preco': 1.2},
    {'nome': 'Bauru Simples', 'preco': 1.3,},
    {'nome': 'Bauru com ovo', 'preco': 1.5},
    {'nome': 'Hambúrguer', 'preco': 1.2},
    {'nome': 'Cheeseburguer', 'preco': 1.3},
    {'nome': 'Refrigerante', 'preco': 1.0}
]

for card in range(len(cardapio)):
    codigo = {'codigo': 100+card}
    cardapio[card].update(codigo)
    
print('Especificação       Código      Preço')
for menu in cardapio:
    print(f"{menu['nome']:<18} {menu['codigo']:^8}{menu['preco']:>8} R$")
    
resp_compra = 'sim'
arr_pedido = []
total = 0
resp_pedido = 's'
while resp_pedido == 's':
    codigo_comida = int(input('\nInsira o código da comida: '))
    qnt_pedida = int(input('Quantidade: '))

    resp_pedido = str(input('Continuar com o pedido? s - n\n'))

    if resp_pedido.lower() in 'nãonao':
        print('Pedido encerrado.')
        
    for pedido in cardapio:
        if codigo_comida == pedido['codigo']:
            total = pedido['preco'] * qnt_pedida
            arr_pedido += [[pedido, qnt_pedida, total]]
soma_total = 0
for result in arr_pedido:
    print(f"{result[1]}X {result[0]['nome']} -> R$ {result[2]:.2f}")
    soma_total += result[2]
print(f'Com o total de R$ {soma_total:.2f}')
