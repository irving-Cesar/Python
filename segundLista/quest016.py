valor_a = int(input('Insira o valor de A: '))
if valor_a != 0:
    valor_b = int(input('Insira o valor de B: '))
    valor_c = int(input('Insira o valor de C: '))

    calc_delta = valor_b**2 - 4 * valor_a * valor_c

    if calc_delta < 0:
        print(calc_delta)
        print('A equação não possui raiz real, finalizando programa.')
        
    elif calc_delta == 0:
        print(calc_delta)
        print('A equação possui apenas uma raiz real.')
        
    elif calc_delta > 0:
        print(calc_delta)
        print('A equação possui duas raizes reais.')
    
else:
    print('Essa não é uma equação de segundo grau, finalizando programa.')
