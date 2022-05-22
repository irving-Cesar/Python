'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles
'''
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 < num2: 
    for i in range(num1, num2+1):
        print(i)
else:
    print('Número 1 maior que o número 2, tente novamente.')
