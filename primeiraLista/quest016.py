'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
import math

area = float(input('Insira o tamanho da área: '))

litro_por_metro = 3
lata_litro = 18
lata_preco = 80

litro_usado = area / litro_por_metro
lata_comprada =  math.ceil(litro_usado / lata_litro)

valor_total = lata_comprada * lata_preco

print('Terá que comprar {} lata(s) no valor total de: {} R$.'.format(lata_comprada, valor_total))
