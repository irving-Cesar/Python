'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia as um conjunto indeterminado de temperaturas, e informe 
ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas
'''

loop = True
cont_i = 0
arr_temps = []
print('0 - Para finalizar')
while loop:
    temp = float(input(f'Insira a temperatura {cont_i+1} em C°: '))
    if temp == 0:
        loop = False
    else:
        if cont_i == 0:
            maior = temp
            menor = temp
        
        if temp > maior:
            maior = temp
        
        if temp < menor:
            menor = temp
            
        arr_temps.append(temp)
        cont_i += 1
        
if cont_i > 0:
    print(f'Menor temperatura: {menor} C° - Maior temperatura: {maior} C°\nMédia: {sum(arr_temps)/len(arr_temps):.1f} C°')
    
    
