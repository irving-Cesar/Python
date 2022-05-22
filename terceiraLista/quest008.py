'''
Faça um programa que leia 5 números e informe a soma e a média dos números
'''

arr_nums = []
for i in range(1, 6):
    num = int(input(f'Insira o {i}° número: '))
    arr_nums.append(num)

print(f'Soma: {sum(arr_nums)} - Média: {sum(arr_nums)/len(arr_nums)}')
