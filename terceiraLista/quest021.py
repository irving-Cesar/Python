'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo
Um número primo é aquele que é divisível somente por ele mesmo e por 1
'''

num = int(input('Insira um numero inteiro: '))
arr = [1]
for i in range(2, num+1):
    if num % i == 0:
        arr.append(num)
        pass
if arr.count(num) > 1:
    print('Não é primo')
else:
    print('É primo')

