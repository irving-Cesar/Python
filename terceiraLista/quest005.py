'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
import math

loop = True
cont_anos = 0
while loop:
    populacao_a = int(input('Insira a população do pais A: '))
    populacao_b = int(input('Insira a população do pais B: '))
    if populacao_a > 0 and populacao_b > 0:
        # taxa1 menor que taxa2, causa erro.
        taxa1 = float(input('Insira o valor da taxa de crescimento do país A: '))
        taxa2 = float(input('Insira o valor da taxa de crescimento do país B: '))
        if taxa1 > 0 and taxa2 > 0 and taxa1 > taxa2:
            taxa1 = (taxa1 / 100) + 1
            taxa2 = (taxa2 / 100) + 1
            while populacao_a != populacao_b and populacao_a < populacao_b:
                populacao_a *= taxa1
                populacao_b *= taxa2
                populacao_a = math.ceil(populacao_a)
                populacao_b = math.ceil(populacao_b)
                cont_anos += 1
        else:
            print('Taxa A menor que Taxa B.')
            continue
        print(f'Levou {cont_anos} anos para o País A igualar/ultrapassar o País B')
        repetir = str(input('\nRepetir operação? s - n\n'))
        if repetir == 'n':
            loop = False
    else:
        print('Insira valores válidos')

