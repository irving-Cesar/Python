'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem 
inversa a ordem lida.
'''

import random


arr_idade = []
arr_altura = []
for i in range(5):
    # idade = int(input('Idade: '))
    # altura = int(input('Altura: '))
    idade = random.randint(1, 80)
    altura = round(random.uniform(1.5, 2), 2)
    arr_idade.append(idade)
    arr_altura.append(altura)
 
print(arr_idade, arr_altura)

print('Tipo reverse A:')
print('Antes:')
print('Array idade: ', arr_idade)
print('Array Altura: ', arr_altura)

print('\nDepois:')
arr_idade_rev = []
arr_alt_rev = []
for i, a in zip(arr_idade, arr_altura):
    i = reversed(str(i))
    a = reversed(str(a))

    arr_idade_rev.append(int(''.join(i)))
    arr_alt_rev.append(float(''.join(a)))
print('Array idade:', arr_idade_rev)
print('Array altura:', arr_alt_rev)

print('\nTipo reverse B:')
print('Antes:')
print('Array idade: ', arr_idade)
print('Array Altura: ', arr_altura)
print('\nDepois:')
print('Array idade: ', list(reversed(arr_idade)))
print('Array Altura: ', list(reversed(arr_altura)))

