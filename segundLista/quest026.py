'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    
Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro.

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
tipo_gasosa = str(input('Qual o combustível quer colocar?\nG - Gasolina\nA - Alcool\n'))
if tipo_gasosa.lower() != 'g' and tipo_gasosa != 'a':
    print('Selecione um valor válido.')
litros = float(input('Quantos litros foram vendidos? '))

preco_gas = 2.5
preco_alc = 1.9

calc1 = 0
calc2 = 0
desc = ''
if tipo_gasosa.lower() == 'g':
    tipo_gasosa = 'Gasolina'
    if litros <= 20:
        desc = '4%'
        calc1 = preco_gas - (preco_gas * 0.04)
        preco_gas = calc1
        calc2 = litros * preco_gas
    elif litros > 20:
        desc = '6%'
        calc1 = preco_gas - (preco_gas * 0.06)
        preco_gas = calc1
        calc2 = litros * preco_gas
else:
    tipo_gasosa = 'Alcool'
    if litros <= 20:
        desc = '3%'
        calc1 = preco_alc - (preco_alc * 0.03)
        preco_alc = calc1
        calc2 = litros * preco_alc
    elif litros > 20:
        desc = '5%'
        calc1 = preco_alc - (preco_alc * 0.05)
        preco_alc = calc1
        calc2 = litros * preco_alc
        
print(f'Tipo {tipo_gasosa}\nDesconto aplicado {desc}\nPreço do combustivel por litro (-{desc}): {calc1} R$\ntotal {calc2:.2f} R$.')
