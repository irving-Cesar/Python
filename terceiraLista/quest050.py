'''
Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
Faça um programa que calcule o valor de H com N termos.
'''

cont_n = int(input('Quantidade: '))
result = 'H = '
soma = 0
for u, n in zip([1]*cont_n, range(1, cont_n+1)):
    if n == 1:
        result += f'{u} + '
    else:
        result += f'{u}/{n}'
        if n < cont_n:
            result += ' + '

    soma += u/n
print(result,end='')
print(f' = {soma:.2f}')
