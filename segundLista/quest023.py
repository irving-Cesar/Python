# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

num = float(input('Insira um número: '))

print('Inteiro' if num % 1 == 0 else 'Decimal')
