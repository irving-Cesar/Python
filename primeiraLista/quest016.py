import math

area = float(input('Insira o tamanho da área: '))

litro_por_metro = 3
lata_litro = 18
lata_preco = 80

litro_usado = area / litro_por_metro
lata_comprada =  math.ceil(litro_usado / lata_litro)

valor_total = lata_comprada * lata_preco

print('Terá que comprar {} lata(s) no valor total de: {} R$.'.format(lata_comprada, valor_total))
