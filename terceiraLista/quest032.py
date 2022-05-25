'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
'''

num = int(input('Fatorial de: '))
v = num
val_string = ''
to_help = num
print(f'{num}! = ',end='')
for i in range(num):
    val_string += f'{v}'
    if i < to_help-1:
        val_string += ' . '
    else:
        val_string += f' = {num}'
    v = (v-1)
    if num * v != 0:
        num  = num * v

print(val_string)
