'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
acidentes de trânsito. Foram obtidos os seguintes dados:
a - Código da cidade;
b - Número de veículos de passeio (em 1999);
c - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e - Qual a média de veículos nas cinco cidades juntas;
f - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

arr_cidades = []

for c in range(5):
    cidade = {}
    nome_city = str(input(f'Insira o nome da cidade {c+1}: '))
    cod_city = int(input('Código da cidade: '))
    qnt_veiculos = int(input('Quantidade de veiculos de passeio: '))
    qnt_acidentes = int(input('Total de acidentes: '))
    
    cidade = {
        'nome' :  nome_city,
        'codigo' : cod_city,
        'veiculos' : qnt_veiculos,
        'acidentes' : qnt_acidentes
    }
    
    arr_cidades.append(cidade)
    
# for x in arr_cidades:
#     print(x)

soma_veiculos = 0
soma_acidentes = 0
cont_city = 0

for cont in range(len(arr_cidades)):
    soma_veiculos += arr_cidades[cont]['veiculos']

    if arr_cidades[cont]['veiculos'] < 2000:
        soma_acidentes += arr_cidades[cont]['acidentes']
        cont_city += 1
        
maior_indice = max(arr_cidades, key=lambda city: city['acidentes'])
menor_indice = min(arr_cidades, key=lambda city: city['acidentes'])

print(f"\nMaior indice de acidentes: {maior_indice['acidentes']} -> Cidade: {maior_indice['nome']}")
print(f"Menor indice: {menor_indice['acidentes']} -> Cidade: {menor_indice['nome']}")
print(f"Média de veículos das cinco cidades: {soma_veiculos/5} - Média de acidentes: {soma_acidentes/cont_city}")
