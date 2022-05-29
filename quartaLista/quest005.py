'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
'''
from random import randint

arr_nums = []
arr_par = []
arr_impar = []

for i in range(20):
    arr_nums.append(randint(1, 100))

for c in arr_nums:
    if c % 2 == 0:
        arr_par.append(c)
    else:
        arr_impar.append(c)

print('nums', arr_nums)
print('ímpar', arr_impar)
print('par', arr_par)
