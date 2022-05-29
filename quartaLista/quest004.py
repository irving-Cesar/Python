'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

arr_caract = ['a', 's', 'b', 'd', 'x', 'e', 'k', 'i', 'l', 'v']
cont = 0
result = ''
for i in arr_caract:
    if i not in 'aeiou':
        result += i + ' '
        cont += 1

print(arr_caract)
print(f'{cont} consoantes -> {result}')
    
    
