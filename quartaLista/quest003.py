'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
arr_notas = []
for i in range(4):
    nota = float(input('Nota: '))
    arr_notas.append(nota)

print(f'Média: {sum(arr_notas)/len(arr_notas)}')
