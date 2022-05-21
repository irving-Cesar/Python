'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
 °Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
 °Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
 °Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
 °Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

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
