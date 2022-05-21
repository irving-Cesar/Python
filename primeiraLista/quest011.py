'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo.
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''

numInt1 = int(input('Insira o primeiro número inteiro: '))
numInt2 = int(input('Insira o segundo número inteiro: '))
numFloat = float(input('Insira o número real: '))

print('a) o produto do dobro do primeiro com metade do segundo: {}'
      '\nb) a soma do triplo do primeiro com o terceiro: {}'
      '\nc) o terceiro elevado ao cubo: {}'.format((numInt1 * 2) * (numInt2 / 2), (numInt1 * 3) + numFloat,
                                                  numFloat ** 3))
