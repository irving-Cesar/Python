'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e 
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

populacao_a = 80000
populacao_b = 200000
taxa1 = 1.03
taxa2 = 1.015
cont_anos = 0

while populacao_a != populacao_b and populacao_a < populacao_b:
    populacao_a *= taxa1
    populacao_b *= taxa2
    populacao_a = int(populacao_a)
    populacao_b = int(populacao_b)
    cont_anos += 1

print(f'Levou {cont_anos} anos para o País A ultrapassar o País B')
