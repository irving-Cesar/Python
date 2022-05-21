'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    1- salários até R$ 280,00 (incluindo) : aumento de 20%
    2- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    3- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    4- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    5- o salário antes do reajuste;
    6- o percentual de aumento aplicado;
    7- o valor do aumento;
    8- o novo salário, após o aumento.
'''
salario_sem_reajuste = float(input('Insira o seu salário atual: '))

salario_reajustado = 0
reajuste_salario = 0
string_percent = ''

if salario_sem_reajuste <= 280:
    salario_reajustado = salario_sem_reajuste * 1.2
    reajuste_salario = salario_sem_reajuste * 0.2
    string_percent = '20% '
    
elif salario_sem_reajuste >= 281 and salario_sem_reajuste <= 700:
    salario_reajustado = salario_sem_reajuste * 1.15
    reajuste_salario = salario_sem_reajuste * 0.15
    string_percent = '15% '
    
elif salario_sem_reajuste >= 701 and salario_sem_reajuste <= 1500 or salario_sem_reajuste >= 1500:
    salario_reajustado = salario_sem_reajuste * 1.1
    reajuste_salario = salario_sem_reajuste * 0.1
    string_percent = '10% '
    
    if salario_sem_reajuste >= 1500:
        reajuste_salario += (int(salario_reajustado) * 0.05)
        salario_reajustado *= 1.05
        string_percent += 'e 5% '


print('Salário sem reajuste: {:.2f} R$\nPercentual aplicado: {}\nReajuste de: {:.2f} R$ \nSalário com reajuste: {:.2f} R$'.format(salario_sem_reajuste, string_percent, reajuste_salario, salario_reajustado))
