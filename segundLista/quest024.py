'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))

nothin = ''
print('\nQual operção deseja realizar?')
user_escolha = int(input('1 - Soma\n2 - Divisão\n3 - Multiplicação\n4 - Subtração\n'))

if user_escolha == 1:
    calc = num1 + num2
elif user_escolha == 2:
    calc = num1 / num2
elif user_escolha == 3:
    calc = num1 * num2
elif user_escolha == 4:
    calc = num1 - num2
else:
    print('Opção inválida.')
    
def operac (num, tipo):
    if tipo == 1:
        return f'{num} é ', 'Par' if num % 2 == 0 else 'Ímpar'
    elif tipo == 2:
        return f'{num} é ', 'Positivo' if num > 0 else 'Negativo'
    elif tipo == 3:
        return f'{num} é ', 'Inteiro' if num % 1 == 0 else 'Decimal'
    

print(f'a) Par ou ímpar: {nothin.join(operac(calc, 1))}\nb) Positivo ou negativo: {nothin.join(operac(calc, 2))}\nc) Inteiro ou decimal: {nothin.join(operac(calc, 3))}\n')
