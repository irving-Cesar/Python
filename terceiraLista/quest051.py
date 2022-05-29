'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''
cont_n = int(input('Quantidade: '))
result = 'S = '
soma = 0
for n, m in zip(range(1, cont_n+1), range(1, cont_n*2, 2)):
    result += f'{n}/{m}'
    if n < cont_n:
        result += ' + '
    soma += n/m
print(result, end='')
print(f' = {soma:.2f}')
