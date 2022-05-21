'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

ht = float(input('Informe as horas trabalhadas durante o mês: '))
qph = float(input('Quanto você recebe por hora: '))
print('Salário: {:.2f} R$.'.format(ht * qph))
