'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

num = int(input('Insira um número inteiro positivo: '))
v = num
for i in range(num):
    v = (v-1)
    if num * v != 0:
        num  = num * v

print(f'Resultado: {num} ')
