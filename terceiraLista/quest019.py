'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''
quant = int(input('Insira a quantidade de números: '))
arr_sum = []
num = -1
for i in range(quant):
    num = -1
    while num < 0 or num > 1000:
        num = int(input(f'Insira o {i+1}° número: '))
        
        if num < 0 or num > 1000:
            print('Insira números entre 0 e 1000.')
        else: 
            if i == 0:
                menor = num
                maior = num
            arr_sum.append(num)
            
            if num > maior:
                maior = num
            
            if num < menor:
                menor = num
        
print(f'{menor} foi o Menor, {maior} o Maior. E {sum(arr_sum)} é soma de todos os valores.')
