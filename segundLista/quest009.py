'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
arr_dec = []
for n in range(1, 4):
    num = int(input('Insira o {}° preço: '.format(n)))
    
    arr_dec.append(num)

arr_dec.sort()
arr_dec = list(reversed(arr_dec))

print(arr_dec)
