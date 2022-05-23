'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares
'''

import random

arr_par = []
arr_impar = []
for i in range(10):
    num = random.randint(1, 101)
    print(num)
    # num = int(input(f'Insira o {i}° número: '))
    if num % 2 == 0:
      arr_par.append(num)
    else:
      arr_impar.append(num)

print(f'{len(arr_par)} Pares e {len(arr_impar)} Inpares')
