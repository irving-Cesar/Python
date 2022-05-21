valor_saque = int(input('Insira o valor do saque: '))
output = ''
arr_result = []
arr_teste = []
arr_tipos = ['cem', 'cinquenta', 'dez', 'cinco', 'um']
saque_fake = valor_saque

if valor_saque >= 10 and valor_saque <= 600:
    nota_cem = valor_saque // 100
    valor_saque -= nota_cem * 100
    
    nota_cinq = valor_saque //  50
    valor_saque -= nota_cinq * 50
    
    nota_dez = valor_saque // 10
    valor_saque -= nota_dez *10
    
    nota_cinco = valor_saque // 5
    valor_saque -= nota_cinco * 5
    
    nota_um = valor_saque // 1
    valor_saque -= nota_um * 1
    
    arr_result += [nota_cem, nota_cinq, nota_dez, nota_cinco, nota_um]
    
    print(f'Para sacar o valor de {saque_fake} R$ foram tiradas: ')
    for x, y in zip(arr_result, range(len(arr_result))):
        if x != 0:
            if x == 1:
                output = f'{x} nota de {arr_tipos[y]}'
            else :
                output = f'{x} notas de {arr_tipos[y]}'
            arr_teste += [output]
    print('\n'.join(arr_teste))
    
else:
    print('Insira um valor de 10 R$ a 600 R$')
