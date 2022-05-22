'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
cont_anos = 0
populacao_a = int(input('Insira a população do pais A: '))
populacao_b = int(input('Insira a população do pais B: '))
if populacao_a > 0 and populacao_b > 0:
    taxa1 = float(input('Insira o valor da taxa de crescimento do país A: '))
    taxa2 = float(input('Insira o valor da taxa de crescimento do país B: '))
    if taxa1 > 0 and taxa2 > 0:
        taxa1 = (taxa1 / 100) + 1
        taxa2 = (taxa2 / 100) + 1
        while populacao_a != populacao_b and populacao_a < populacao_b:
            populacao_a *= taxa1
            populacao_b *= taxa2
            populacao_a = int(populacao_a)
            populacao_b = int(populacao_b)
            cont_anos += 1

    print(f'Levou {cont_anos} anos para o País A igualar/ultrapassar o País B')
else:
    print('Insira valores válidos')

