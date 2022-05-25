'''
Faça um programa que calcule o número médio de alunos por turma
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma
As turmas não podem ter mais de 40 alunos
'''

arr_turma = []
turmas = int(input('Informe a quantidade de turmas: '))

for i in range(turmas):
    alunos = 41
    while alunos > 40:
        alunos = int(input(f'Insira a quantidade de alunos na turma {i+1}°: '))
    arr_turma.append(alunos)

print(f'Média {sum(arr_turma)/turmas}')
