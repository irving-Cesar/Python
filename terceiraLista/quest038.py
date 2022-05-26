'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o salário
atual desse funcionário. Após concluir isto, altere o programa permitindo que
o usuário digite o salário inicial do funcionário.
'''

sal_inicial = float(input('Insira o seu salário inicial: '))
ano = 1995
aumento_perc = 0.015
p = aumento_perc
for i in range(ano, 2022):
    print(f'ano {i} tem salario: {sal_inicial:.2f}')
    sal_inicial += (sal_inicial * aumento_perc)
    aumento_perc += p
print(f'Salario atual: {sal_inicial:.2f} R$')
