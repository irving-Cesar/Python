'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

arr_perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
arr_respostas = []
resposta = ''

print('Responda com sim ou não.')
for i, k in zip(arr_perguntas, range(len(arr_perguntas))):
    resposta = ''
    while resposta != 'sim' and resposta != 'não':
        resposta = str(input(f'{k+1}° pergunta: {i}\nR - '))
        resposta = resposta.lower()
    arr_respostas.append(resposta)
    
if arr_respostas.count('sim') == 5:
    print('Você é o Assassino!')
elif arr_respostas.count('sim') >= 3 and arr_respostas.count('sim') <= 4:
    print('Você é o Cúmplice!')
elif arr_respostas.count('sim') == 2:
    print('Você é Suspeito!')
else:
    print('Inocente!')
        
