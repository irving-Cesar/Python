'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados 
por meio de código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos
    Para finalizar o conjunto de votos tem-se o valor zero.
'''

arr_candidato = []
voto_branco = 0
voto_nulo = 0
votos_totais = 0
arr_nome_candidatos = ['José', 'Victória', 'Ricador', 'Primo Rico']

# cadastrando candidatos
for cadastro in range(1, 5):
    candidato_dict = {}
    candidato_dict = {
        'nome': arr_nome_candidatos[cadastro-1],
        'num': cadastro,
        'votos': 0
    }
    arr_candidato.append(candidato_dict)
    
print('CANDIDATOS:')
for candidato in arr_candidato:
    print('-~'*15)
    print(f"Nome: {candidato['nome']} - Número: {candidato['num']}")
    print('-~'*15)
print('5 - Voto Nulo\n6 - Voto Em Branco')

voto = 1
# realizando votação e verificando se o voto é válido
while voto != 0:
    voto = int(input('\nEm quem deseja votar (Número)?\nVoto - '))
    if voto == 0:
        break
    else: 
        if voto < 0 or voto > 6:
            print('Por favor, insira um número VÁLIDO!')
            continue
        
        for x in arr_candidato:
            if voto == x['num']:
                x['votos'] += 1
                print('Voto deferido!')
             
        if voto == 5:
            voto_nulo += 1
            print('Voto deferido!')
            
        elif voto == 6:
            voto_branco += 1
            print('Voto deferido!')
            
        votos_totais += 1
    
print('\nQuantidade de VOTOS:')

for candidato in arr_candidato:
    print('-~'*20)
    print(f"\nNome: {candidato['nome']} - Obteve : {candidato['votos']} votos")
print(f'\nVotos Nulos: {voto_nulo}\nVotos em Branco: {voto_branco}')
print('-~'*20)
print(f'PERCENTAGEM (sobre o total de {votos_totais} votos):')
print(f'-Votos Nulos {(voto_nulo*100)/votos_totais:.2f}%')
print(f'-Votos em Branco {(voto_branco*100)/votos_totais:.2f}%')

