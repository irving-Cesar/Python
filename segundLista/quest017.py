'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
'''

ano = int(input('Insira ano que desejar: '))

calc4 = ano % 4
calc100 = ano % 100
calc400 = ano % 400

if calc4 == 0 and calc100 != 0 or calc400 == 0:
    print('{} é BISSEXTO.'.format(ano))
else:
    print('{} não é BISSEXTO.'.format(ano))
