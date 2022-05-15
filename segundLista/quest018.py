dia = False
mes = False
ano = False

print('formato da data: dd/mm/aaaa.')
data_dia = int(input('Dia: '))
data_mes = int(input('Mês: '))
data_ano = int(input('Ano: '))

if data_dia != 0:
    if data_dia >= 1 and data_dia <= 31:
        dia = True

if data_mes != 0:
    if data_mes >= 1 and data_mes <= 12:
        mes = True

if int(data_ano) != 0:
    if data_ano >= 1000 and data_ano <= 9999:
        ano = True

print('Data digitada:')
print('{}/{}/{}'.format(data_dia, data_mes, data_ano))
if dia and mes and ano:
    print('Data válida.')
else:
    print('Data inválida.')
