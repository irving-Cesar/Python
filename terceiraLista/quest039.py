'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro 
representando o número do aluno e o segundo representando a sua altura em 
centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do
aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
'''
import random

arr_alunos = []
for i in range(10):
    aluno_num = random.randint(1000, 9999)
    altura_aluno = round(random.uniform(1.5, 2.1), 2)
    # aluno_num = int(input('Insira o seu número: '))
    # altura_aluno = float(input('Agora a sua altura: '))
    
    arr_alunos.append([aluno_num, altura_aluno])
    print('-~'*10)
    print(f'Número do aluno {aluno_num} - Altura do Aluno: {altura_aluno}')
    print('-~'*10)

maior_alt = max(arr_alunos, key=lambda alt: alt[1])

print(f'\nMAIOR altura: {maior_alt[1]} - Número do aluno: {maior_alt[0]}')
