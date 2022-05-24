'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados
'''
print('-*'*20)
quantidade = int(input('Insira o um número inteiro: '))
print('-*'*20)
print('\n')
arr_primos = []
arr_cont_div = []
contador_primo = 0
contador_div = 0

for i in range(2, quantidade+1):
    contador_primo = 0
    for j in range(1, i+1):
        if i % j == 0:
            contador_primo += 1
            contador_div += 1
    if contador_primo == 2:
        arr_cont_div.append(contador_div)
        arr_primos.append(i)
a =''
for x, y in zip(arr_primos, arr_cont_div):
    print('|','-~'*30+'|')
    print(f'''{a: >6}Número primo: {x} - Divisões executadas (total): {y}''')
    print('|','-~'*30+'|')
