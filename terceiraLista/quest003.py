'''
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
'''

nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil_valores = ['s', 'c', 'v', 'd']
estado_civil = ''
cont = 1
loop = True

while loop:
    if cont == 1:
        nome = str(input('Insira o seu nome: '))
        if len(nome) > 3:
            cont = 2
        else:
            print('Digite pelo menos 4 catacteres.\n')
            
    elif cont == 2:
        idade = int(input('Insira a sua idade: '))
        if idade >= 0 and idade <= 150:
            cont = 3
        else:
            print('Idade inválida.\n')
            
    elif cont == 3:
        salario = float(input('Insira seu salário: '))
        if salario > 0:
            cont = 4
        else:
            print('Salário inválido.\n')
            
    elif cont == 4:
        sexo = str(input('Informe o seu sexo (F ou M): '))
        if sexo.lower() == 'f' or sexo.lower() == 'm':
            cont = 5
        else:
            print('Sexo inválido.\n')
    
    elif cont == 5:
        print('Seu estado civil:\nS - Solteiro(a)\nC - Casado(a)\nV - Viúvo(a)\nD - Divorciado(a)')
        estado_civil = str(input(''))
        if estado_civil.lower() in estado_civil_valores:
            print('Sucesso!')
            loop = False
            cont = 0
        else:
            print('Esse estado civil não existe.\n')
