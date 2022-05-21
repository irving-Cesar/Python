'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''
c = float(input('Insira o grau em Celsius: '))
f = (c * 9 / 5) + 32
print('Graus em F: {:.1f}°'.format(f))
