'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores
'''
quant = int(input('Insira a quantidade de números: '))
arr_sum = []
for i in range(quant):
    num = int(input(f'Insira o {i+1}° número: '))
    if i == 0:
        menor = num
        maior = num
    arr_sum.append(num)
    
    if num > maior:
        maior = num
    
    if num < menor:
        menor = num
        
print(f'{menor} foi o Menor, {maior} o Maior. E {sum(arr_sum)} é soma de todos os valores.')
