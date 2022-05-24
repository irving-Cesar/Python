'''
Faça um programa que calcule o mostre a média aritmética de N notas
'''
n = int(input('Insira a quantidade de notas: '))
arr_notas = []
for i in range(n):
    nota = int(input(f'Insira a {i+1}° nota: '))
    arr_notas.append(nota)

print(f'Média: {(sum(arr_notas)/len(arr_notas))}')
