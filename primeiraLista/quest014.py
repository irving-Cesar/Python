pesoPeixe = float(input('Insira o peso total dos peixes: '))
pesoMax = 50
mult = 4
calcM = (pesoPeixe - pesoMax) * mult

if pesoPeixe > pesoMax:
    print('Peso além do limite: {}Kg\nMulta a ser paga: {} R$'.format((pesoPeixe - pesoMax), calcM))

print('Bom trabalho!')
