area = float(input('Insira o tamanho da área: '))

litro_por_metro = 3
lata_litro = 18
lata_preco = 80

lata_comprada = area / lata_litro
lata_comprada = int(lata_comprada)

if not (area % lata_litro) == 0:
    lata_comprada+=1

valor_total = lata_comprada * lata_preco

print('Valor a ser pago: {:.2f} R$, quantiadade de latas compradas {}.'.format(valor_total, int(lata_comprada)))
