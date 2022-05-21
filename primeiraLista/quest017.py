'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a) comprar apenas latas de 18 litros;
b) comprar apenas galões de 3,6 litros;
c) misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math

area = float(input('Insira o tamanho da área: '))
folga_area = (area * 0.1) + area
litro_por_metro = 6
litro_usado = folga_area / litro_por_metro
print('{:.3f} litros totais.'.format(litro_usado))

# usando lata
litro_lata = 18
preco_lata = 80
quantidade_comprada_latas =  math.ceil(litro_usado / litro_lata)
valor_total_lata = quantidade_comprada_latas * preco_lata

print('Terá que comprar {} lata(s) no valor total de: {} R$.'.format(quantidade_comprada_latas, valor_total_lata))

# usando galao
litro_galao = 3.6
preco_galao = 25
quantidade_comprada_galao =  math.ceil(litro_usado / litro_galao)
valor_total_galao = quantidade_comprada_galao * preco_galao

print('Terá que comprar {} galao(s) no valor total de: {} R$.'.format(quantidade_comprada_galao, valor_total_galao))

# misturando galao x lata
quantidade_comprada_latas = math.floor(litro_usado / litro_lata)
valor_por_latas = quantidade_comprada_latas * 80
restando_litros =  quantidade_comprada_latas % litro_lata
galao_resto = math.ceil(restando_litros / litro_galao)
valor_total_misturado = (valor_por_latas + (galao_resto * preco_galao))

print('Misturando ficou {} lata(s) e {} galao(s). Totalizando {} R$.'.format(math.floor(quantidade_comprada_latas), galao_resto, valor_total_misturado))
