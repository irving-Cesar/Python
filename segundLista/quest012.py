valor_por_hora = float(input('Quanto ganha por hora: '))
horas_trabalhas_mes = float(input('Horas trabalhadas no mês: '))

salario_bruto = valor_por_hora * horas_trabalhas_mes
fgts = salario_bruto * 0.11
calc_inss = (salario_bruto * 0.1)
desc_inss_ir = 0
calc_ir = 0

if salario_bruto >= 901 and salario_bruto <= 1500:
    calc_ir = salario_bruto * 0.05
    desc_inss_ir = salario_bruto - (calc_ir + calc_inss)
    
elif salario_bruto >= 1501 and salario_bruto <= 2500:
    calc_ir = salario_bruto * 0.1
    desc_inss_ir = salario_bruto - (calc_ir + calc_inss)
  
elif salario_bruto > 2500:
    calc_ir = salario_bruto * 0.2
    desc_inss_ir = salario_bruto - (calc_ir + calc_inss)
    
print('Salário bruto: {:.2f} R$\nIR: {:.2f} R$\nINSS: {:.2f} R$\nFGTS: {:.2f} R$\nSalário líquido: {:.2f} R$'.format(salario_bruto, calc_ir, calc_inss, fgts, desc_inss_ir))
