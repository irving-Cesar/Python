for n in range(1, 4):
    num = int(input('Insira o {}° numero: '.format(n)))
    if n == 1:
        maior = num
        
    if num > maior:
        maior = num
    
print('Maior {}'.format(maior))
