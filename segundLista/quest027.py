'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

maca_kg = float(input('Insira os kgs da Maça: '))
morango_kg = float(input('Insira os kgs do Morango: '))

preco_morango = 0
preco_maca = 0
total_maca = 0
total_morango = 0
total = 0
soma_kg = maca_kg + morango_kg

# maça
if maca_kg <= 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5
total_maca = maca_kg * preco_maca

# morango
if morango_kg <= 5:
    preco_morango = 2.5
else:
    preco_morango = 2.2
total_morango = morango_kg * preco_morango

total = total_morango + total_maca

if total > 25 or soma_kg > 8:
    total = total - (total * 0.1)

print(f'A compra foi de:\n{morango_kg} kg de Morangos\n{maca_kg} kg de Maças\n{soma_kg} kg Totais\nNo valor de {total:.2f} R$')

