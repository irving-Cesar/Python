'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7
'''
alt = float(input('Insira a sua altura: '))
imcH = (72.7 * alt) - 58
imcM = (62.1 * alt) - 44.7

print('Peso ideal:\na) homem: {:.2f}\nb) mulher: {:.2f}'.format(imcH, imcM))
