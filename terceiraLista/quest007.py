'''
Faça um programa que leia 5 números e informe o maior número.
'''

for i in range(1, 6):
    num = int(input(f'Insira o {i}° número: '))
    if i == 1:
        maior = num
    
    if num > maior:
        maior = num

print(f'Maior num: {maior}')
