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
