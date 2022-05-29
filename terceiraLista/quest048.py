'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
'''

num = int(input('Insira um numero inteiro positivo: '))
num = str(num)

reverse = ''
for n in range(len(num)):
    reverse += num[-n-1]
print(reverse)
