'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
from math import pi
r = float(input('Insira o raio do círculo: '))
calcA = pi * r**2
print('Área do círculo: {:.3f}'.format(calcA))
