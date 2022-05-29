'''
Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno, imprima o 
número de alunos com média maior ou igual a 7.0.
'''

arr_media = []
for a in range(10):
    med = 0
    print('Nota do aluno', a+1)
    for n in range(4):
        nota = float(input('Nota: '))
        med += nota
    med = med/4
    arr_media.append(med)

cont_pos = 0
for i in arr_media:
    if i >= 7:
        cont_pos += 1

print(f'{cont_pos} alunos com notas maiores/igual a 7.')
