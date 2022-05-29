'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos
votos restantes. Você deve fazer um programa que receba o nome do ginasta 
e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e 
depois informe a sua média, conforme a descrição acima informada (retirar
o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informados ordenadas. Um exemplo de saída do programa deve 
ser conforme o exemplo abaixo:

    Atleta: Aparecido Parente
    Nota: 9.9
    Nota: 7.5
    Nota: 9.5
    Nota: 8.5
    Nota: 9.0
    Nota: 8.5
    Nota: 9.7
    
    Resultado final:
    Atleta: Aparecido Parente
    Melhor nota: 9.9
    Pior nota: 7.5
    Média: 9,04
'''

loop = True
while loop:
    arr_notas = []
    nome_atleta = str(input('Atleta: '))
    if nome_atleta.strip() == '':
        print('Finalizado.')
        break
    for n in range(1, 8):
        nota = float(input('Nota: '))
        arr_notas.append(nota)
    
    maior_nota = max(arr_notas, key=lambda nota: nota)
    menor_nota = min(arr_notas, key=lambda nota: nota)
    
    print(f'\nResultado Final: \nAtleta: {nome_atleta}\nMelhor nota: {maior_nota}')
    print(f'Pior nota: {menor_nota}')
    del arr_notas[arr_notas.index(maior_nota)]
    del arr_notas[arr_notas.index(menor_nota)]
    media = 0
    for m in arr_notas:
        media += m
        
    media = media/len(arr_notas)
    print(f'Média: {media:.2f}\n')
        
