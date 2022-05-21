'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''
pesoPeixe = float(input('Insira o peso total dos peixes: '))
pesoMax = 50
mult = 4
calcM = (pesoPeixe - pesoMax) * mult

if pesoPeixe > pesoMax:
    print('Peso além do limite: {}Kg\nMulta a ser paga: {} R$'.format((pesoPeixe - pesoMax), calcM))

print('Bom trabalho!')
