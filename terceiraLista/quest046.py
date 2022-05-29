'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são 
eliminados. O seu resultado fica sendo a média dos três valores restantes. Você 
deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe a média dos saltos conforme a descrição
acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na
ordem da execução, portanto não são ordenados. O programa deve ser encerrado
quando não for informado o nome do atleta. A saída do programa deve ser 
conforme o exemplo abaixo:

    Atleta: Rodrigo Curvêllo
    
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m
    
    Melhor salto:  6.5 m
    Pior salto: 5.3 m
    Média dos demais saltos: 5.9 m
    
    Resultado final:
    Rodrigo Curvêllo: 5.9 m
'''
loop = True
cont_atleta = 0
while loop:
    cont_atleta += 1
    arr_saltos_atleta = []
    
    nome_atleta = str(input('Atleta: '))
    print('')
    
    if nome_atleta.strip() == '':
        print('Programa finalizado!')
        loop = False
        break
    
    for i in range(1, 6):
        saltos = float(input(f'Insira o {i}° salto: '))
        arr_saltos_atleta.append(saltos)

    maior_salto = max(arr_saltos_atleta, key=lambda salto: salto)
    menor_salto = min(arr_saltos_atleta, key=lambda salto: salto)
    print(f'\nMelhor salto: {maior_salto} m\nPior Salto: {menor_salto} m')
   
    del arr_saltos_atleta[arr_saltos_atleta.index(maior_salto)]
    del arr_saltos_atleta[arr_saltos_atleta.index(menor_salto)]

    media = 0
    for m in arr_saltos_atleta:
        media += m
    media = media/len(arr_saltos_atleta)
    print(f'Média dos demais Saltos: {media:.1f} m\n')
    print('Resultado final:')
    print(f'{nome_atleta}: {media:.1f} m\n')
    
