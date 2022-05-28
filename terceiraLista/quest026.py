'''
Numa eleição existem três candidatos
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato
'''
from random import randint
eleitores =  int(input('Insira a quantidade de eleitores: '))
arr_candi = [
    {
        'nome': 'José Bezerra',
        'partido' : 'TMJ',
        'num' : 167,
        'votos' : 0
    },
    {
        'nome': 'Márcia Cavalvante',
        'partido' : 'FML',
        'num' : 556,
        'votos' : 0
    },
    {
        'nome': 'Rogerína Santana',
        'partido' : 'SSP',
        'num' : 865,
        'votos' : 0
    }
]
arr_num_vots = []
for k in arr_candi:
    arr_num_vots.append(k['num']) # guardar num dos candidatos
    
form = ''
print(f'{form: >6}CANDIDATOS:')
for candidato in arr_candi:
    print('-~'*15)
    print(f"|{form: ^5}Nome: {candidato['nome']}\n|{form: ^5}Partido: {candidato['partido']}\n|{form: ^5}Numéro : {candidato['num']}")
    print('-~'*15)
    
for i in range(eleitores):
    cont = 0
    while cont == 0:
        # voto = int(input(f'Eleitor {i+1}, em quem deseja votar (Número)?\nVoto - '))
        voto = arr_num_vots[randint(0, 2)] # escolher aleatoriamente os numeros dos candidatos
        for x in arr_candi:
            if voto == x['num']:
                x['votos'] += 1
                cont = 1
                break
        if cont == 0:
            print('Insira um número correto.\n')

print('\nQuantidade de VOTOS:')
for candidato in arr_candi:
    print('-~'*15)
    print(f"{form: ^5}Nome: {candidato['nome']}\n{form: ^5}Obteve : {candidato['votos']} votos")


