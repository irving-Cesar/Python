'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
°Salário Bruto até 900 (inclusive) - isento
°Salário Bruto até 1500 (inclusive) - desconto de 5%
°Salário Bruto até 2500 (inclusive) - desconto de 10%
°Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
 No exemplo o valor da hora é 5 e a quantidade de hora é 220.
 
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

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

else:
    calc_inss = 0
    desc_inss_ir = salario_bruto
    
print('Salário bruto: {:.2f} R$\n(-) IR: {:.2f} R$\n(-) INSS: {:.2f} R$\nFGTS: {:.2f} R$\nSalário líquido: {:.2f} R$'.format(salario_bruto, calc_ir, calc_inss, fgts, desc_inss_ir))
