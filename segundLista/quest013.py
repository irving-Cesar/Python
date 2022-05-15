arr_semanas = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

for d in range(len(arr_semanas)):
    print('{} - {}'.format(d+1, arr_semanas[d]))
semana = int(input('Escolha o dia da semana: '))

if semana >=0 and semana <= 7:
    print('Dia escolhido: {}'.format(arr_semanas[semana-1]))
else:
    print('Valor inválido.')
