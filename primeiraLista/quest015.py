'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
      + Salário Bruto : R$
      - IR (11%) : R$
      - INSS (8%) : R$
      - Sindicato ( 5%) : R$
      = Salário Liquido : R$
'''
horasTrab = float(input('Informe as horas trabalhadas durante o mês: '))
ganhaHora = float(input('Quanto você recebe por hora: '))

calcB = horasTrab * ganhaHora
calcIr = (calcB * 0.11)
calcINSS = (calcB * 0.08)
calcSind = (calcB * 0.05)
calcSL = calcB - (calcIr + calcINSS + calcSind)

print('')
print('a) salário bruto: {:.2f} R$'
      '\nb) quanto pagou ao imposto de renda: {:.2f} R$'
      '\nc) quanto pagou ao INSS: {:.2f} R$'
      '\nd) quanto pagou ao sindicato: {:.2f} R$'
      '\ne) o salário líquido: {:.2f} R$'.format(calcB, calcIr, calcINSS, calcSind, calcSL))
