'''
Faça um programa que calcule o valor total investido por um colecionador 
em sua coleção de CDs e o valor médio gasto em cada um deles
O usuário deverá informar a quantidade de CDs e o valor para em cada um
'''
cds = int(input('Insira a quantidade de cds: '))
arr_cds = []

for i in range(cds):
    valor = float(input(f'Valor do cd {i+1}: '))
    arr_cds.append(valor)

print(f'Valor total: {sum(arr_cds):.2f} R$ - Média: {sum(arr_cds)/len(arr_cds)}')
