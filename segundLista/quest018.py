'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

# dia-mes -> ser diferente de 0 e nao passar do valor maximo
# ano -> ser diferente de 0 e estar entre 1900 - 9999
dia = False
mes = False
ano = False

print('formato da data: dd/mm/aaaa.')
data_dia = str(input('Dia: '))
data_mes = str(input('Mês: '))
data_ano = int(input('Ano: '))

if int(data_dia) != 0:
    if int(data_dia) >= 1 and int(data_dia) <= 31:
        dia = True

if int(data_mes) != 0:
    if int(data_mes) >= 1 and int(data_mes) <= 12:
        mes = True

if data_ano != 0:
    if data_ano >= 1900 and data_ano <= 9999:
        ano = True

print('Data digitada:')
print('{}/{}/{}'.format(data_dia, data_mes, data_ano))
if dia and mes and ano:
    print('Data válida.')
else:
    print('Data inválida.')
