'''
Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível 
apenas por um e por ele mesmo. Faça um programa que peça um número inteiro 
e determine se ele é ou não um número primo.
'''

num = int(input('Insira um número inteiro: '))
contador = 0

for i in range(1, num+1):
    if num % i == 0:
        contador += 1
    
if contador == 2:
    print('Número primo')
else:
    print('Não é primo')
    
