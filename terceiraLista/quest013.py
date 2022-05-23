'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem
'''

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
v = num1
for x in range(num2-1):
    num1 = num1 * v
    
print(num1)
