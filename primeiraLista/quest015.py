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
