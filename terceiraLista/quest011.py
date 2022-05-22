'''
Altere o programa anterior para mostrar no final a soma dos números
'''
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
result = 0
if num1 < num2: 
    for i in range(num1, num2+1):
        print(i)
        result += i
    print('Soma = ', result)
else:
    print('Número 1 maior que o número 2, tente novamente.')
