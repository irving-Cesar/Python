'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números
'''
from random import randint

arr_nums = []
for i in range(5):
    arr_nums.append(randint(1, 100))

multi = 1
for m in arr_nums:
    multi *= m

print('soma', sum(arr_nums))
print('multiplicação', multi)
print('nums', arr_nums)
