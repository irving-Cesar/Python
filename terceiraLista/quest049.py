'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
'''
cont_n = int(input('Quantidade: '))
result = 'S = '
to_help = cont_n
for n, m in zip(range(1, cont_n+1), range(1, cont_n+1, 2)):
    result += f'{n}/{m}'
    if m < to_help-1:
        result += ' + '
    else:
        result += '.'
    
print(result)
