'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
notas = []
for n in range(1, 5):
    nota = float(input('Insira a {}° nota: '.format(n)))
    notas.append(nota)
print('Média: {}'.format(sum(notas)/(len(notas))))
