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
        salario_reajustado = salario_sem_reajuste * 1.15
        reajuste_salario += salario_sem_reajuste * 0.05
        string_percent += 'e 5% '


print('Salário sem reajuste: {:.2f} R$
      '\nPercentual aplicado: {}
      '\nReajuste de: {:.2f} R$
      '\nSalário com reajuste: {:.2f} R$'.format(salario_sem_reajuste, string_percent, reajuste_salario, salario_reajustado))
