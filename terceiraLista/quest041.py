'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
valor da parcela

Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''

valor_divida = float(input('Insira o valor da dívida: '))
divida_val = valor_divida
valor_juros = 0
valor_parcela = 0
juros = 0
arr_parcelas = [1, 3, 6, 9, 12]
fmt = ''
print('Valor da dívida - Valor dos Juro - Quantidade de parcelas - Valor da Parcela')
for i in arr_parcelas:
    if i == 3:
        juros += 0.1
    elif i > 3:
        juros += 0.05
        
    valor_juros = (divida_val * juros)
    valor_divida = divida_val + valor_juros
    
    print(f'\nR$ {valor_divida:.2f}{fmt: ^15}R$ {valor_juros:.2f}{fmt: ^15}{i}{fmt: ^15}R$ {valor_divida / i:.2f}')
    

    
    
