'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''
alt = float(input('Insira a sua altura: '))
imc = (72.7 * alt) - 58
print('Seu imc é: {}'.format(imc))
