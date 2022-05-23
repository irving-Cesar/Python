'''
Altere o programa de cálculo dos números primos, informando, 
caso o número não seja primo, por quais número ele é divisível
'''

num = int(input('Insira um numero inteiro: '))
arr = [1]
arr_div = []
for i in range(2, num+1):
    if num % i == 0:
        arr.append(num)
        arr_div.append(i)
        pass
if arr.count(num) > 1:
    print('Não é primo')
    str_div = [str(int) for int in arr_div]
    str_div = ', '.join(str_div)
    print(f'Divisível por {str_div}')
else:
    print('É primo')

